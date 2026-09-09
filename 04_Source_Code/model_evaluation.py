import json
import pickle
import numpy as np
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    roc_curve,
    classification_report
)
from feature_extraction import FeatureExtractor


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_PATH = “outputs/svm_lbp_hog_model.pkl”
SPLIT_PATH = "outputs/dataset_splits.json"


# ============================================================
# LOAD MODEL
# ============================================================

def load_model(model_path):
    with open(model_path, "rb") as file:
        model_information = pickle.load(file)
    return model_information


# ============================================================
# LOAD TEST DATA
# ============================================================

def load_test_records(split_path):
    with open(split_path, "r") as file:
        split_data = json.load(file)
    return split_data["test"]


# ============================================================
# CALCULATE PAD METRICS
# ============================================================

def calculate_pad_metrics(y_true, y_pred):
    """
    Calculate PAD-specific metrics: APCER, BPCER, ACER.
    
    APCER (Attack Presentation Classification Error Rate):
        False Negative Rate - Percentage of attacks misclassified as genuine
        
    BPCER (Bona Fide Presentation Classification Error Rate):
        False Positive Rate - Percentage of genuine samples misclassified as attacks
        
    ACER (Average Classification Error Rate):
        Average of APCER and BPCER
    
    Args:
        y_true: True labels (0=Genuine, 1=Puppet Attack)
        y_pred: Predicted labels
    
    Returns:
        Dictionary with APCER, BPCER, ACER
    """
    # Confusion matrix
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    
    # APCER = FN / (TP + FN) - Missed attacks
    apcer = fn / (tp + fn) if (tp + fn) > 0 else 0
    
    # BPCER = FP / (TN + FP) - False alarms on genuine
    bpcer = fp / (tn + fp) if (tn + fp) > 0 else 0
    
    # ACER = (APCER + BPCER) / 2
    acer = (apcer + bpcer) / 2
    
    return {
        'apcer': apcer,
        'bpcer': bpcer,
        'acer': acer,
        'false_negatives': fn,
        'false_positives': fp,
        'true_positives': tp,
        'true_negatives': tn
    }


# ============================================================
# EVALUATE MODEL
# ============================================================

def evaluate_model(model, X_test, y_test):
    """
    Full evaluation with standard metrics + PAD metrics.
    """
    predictions = model.predict(X_test)
    probabilities = model.decision_function(X_test)  # For ROC-AUC
    
    # ============================================================
    # Confusion Matrix
    # ============================================================
    cm = confusion_matrix(
        y_test,
        predictions,
        labels=["Genuine", "Puppet"]
    )
    
    print("\n======================================")
    print("CONFUSION MATRIX")
    print("======================================")
    print("              Predicted")
    print("            Genuine  Puppet")
    print(f"Actual Genuine  {cm[0][0]:8d}  {cm[0][1]:7d}")
    print(f"Actual Puppet   {cm[1][0]:8d}  {cm[1][1]:7d}")
    
    # ============================================================
    # Standard Metrics
    # ============================================================
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, pos_label="Puppet", zero_division=0)
    recall = recall_score(y_test, predictions, pos_label="Puppet", zero_division=0)
    f1 = f1_score(y_test, predictions, pos_label="Puppet", zero_division=0)
    roc_auc = roc_auc_score(y_test, probabilities)
    
    # ============================================================
    # PAD Metrics
    # ============================================================
    pad_metrics = calculate_pad_metrics(y_test, predictions)
    
    # ============================================================
    # Display Results
    # ============================================================
    print("\n======================================")
    print("STANDARD CLASSIFICATION METRICS")
    print("======================================")
    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1-Score : {f1:.4f}")
    print(f"ROC-AUC  : {roc_auc:.4f}")
    
    print("\n======================================")
    print("PAD-SPECIFIC METRICS")
    print("======================================")
    print(f"APCER (Attack Error)  : {pad_metrics['apcer']:.4f}")
    print(f"BPCER (Genuine Error) : {pad_metrics['bpcer']:.4f}")
    print(f"ACER  (Average Error) : {pad_metrics['acer']:.4f}")
    
    # ============================================================
    # Classification Report
    # ============================================================
    print("\n======================================")
    print("CLASSIFICATION REPORT")
    print("======================================")
    print(
        classification_report(
            y_test,
            predictions,
            labels=["Genuine", "Puppet"],
            zero_division=0
        )
    )
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'roc_auc': roc_auc,
        'apcer': pad_metrics['apcer'],
        'bpcer': pad_metrics['bpcer'],
        'acer': pad_metrics['acer'],
        'confusion_matrix': cm.tolist()
    }


# ============================================================
# MAIN
# ============================================================

def main():
    print("======================================")
    print("MODEL EVALUATION")
    print("======================================")
    
    # 1. LOAD MODEL
    model_information = load_model(MODEL_PATH)
    model = model_information["model"]
    print(f"\nLoaded model with C = {model_information['best_C']}")
    
    # 2. LOAD TEST RECORDS
    test_records = load_test_records(SPLIT_PATH)
    print(f"Test images: {len(test_records)}")
    
    # 3. CREATE FEATURE EXTRACTOR
    print("\nCreating LBP + HOG feature extractor...")
    extractor = FeatureExtractor(
        lbp_points=model_information["lbp_num_points"],
        lbp_radius=model_information["lbp_radius"],
        hog_orientations=9
    )
    
    # 4. EXTRACT TEST FEATURES
    print("Extracting test features...")
    X_test, y_test = extractor.extract_features_batch(test_records)
    
    # 5. EVALUATE
    results = evaluate_model(model, X_test, y_test)
    
    # 6. SAVE RESULTS
    with open("outputs/evaluation_results.json", "w") as file:
        json.dump(results, file, indent=4)
    print("\nResults saved to: outputs/evaluation_results.json")
    
    return results


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()
