import os
import pickle
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

from data_loader import (
    load_dataset,
    split_dataset,
    print_split_information,
    check_participant_leakage,
    save_splits
)
from feature_extraction import FeatureExtractor


# ============================================================
# CONFIGURATION
# ============================================================

DATASET_PATH = "dataset"
OUTPUT_DIR = "outputs"
MODEL_PATH = os.path.join(OUTPUT_DIR, "svm_lbp_hog_model.pkl")

# SVM hyperparameter grid for tuning
C_VALUES = [0.01, 0.1, 1.0, 10.0, 100.0]

# Feature extraction parameters (must match feature_extraction.py)
LBP_POINTS = 24
LBP_RADIUS = 8
HOG_ORIENTATIONS = 9


# ============================================================
# TRAIN SVM
# ============================================================

def train_svm(X_train, y_train, C):
    """Train Linear SVM with given C parameter."""
    model = LinearSVC(
        C=C,
        random_state=42,
        max_iter=5000,
        dual=False
    )
    model.fit(X_train, y_train)
    return model


# ============================================================
# MAIN TRAINING PIPELINE
# ============================================================

def main():
    print("=" * 70)
    print(" FINGERPRINT PUPPET ATTACK DETECTION")
    print(" LBP + HOG Fusion Features with SVM")
    print("=" * 70)

    # ============================================================
    # 1. LOAD DATASET
    # ============================================================
    print("\n[1] Loading dataset...")
    records = load_dataset(DATASET_PATH)
    print(f"    Total images: {len(records)}")

    if len(records) == 0:
        print("ERROR: No images found. Check your dataset path.")
        return

    # ============================================================
    # 2. SPLIT DATASET (Participant-level)
    # ============================================================
    print("\n[2] Splitting dataset (70/10/20 at participant level)...")
    train_records, validation_records, test_records = split_dataset(
        records,
        train_size=0.70,
        validation_size=0.10,
        test_size=0.20,
        random_state=42
    )

    print_split_information(train_records, validation_records, test_records)
    check_participant_leakage(train_records, validation_records, test_records)
    save_splits(train_records, validation_records, test_records)

    # ============================================================
    # 3. CREATE FEATURE EXTRACTOR (LBP + HOG FUSION)
    # ============================================================
    print("\n[3] Creating LBP + HOG feature extractor...")
    extractor = FeatureExtractor(
        lbp_points=LBP_POINTS,
        lbp_radius=LBP_RADIUS,
        hog_orientations=HOG_ORIENTATIONS
    )

    # ============================================================
    # 4. EXTRACT TRAINING FEATURES
    # ============================================================
    print("\n[4] Extracting training features (LBP + HOG)...")
    X_train, y_train = extractor.extract_features_batch(train_records)
    X_train_scaled = extractor.fit_transform(X_train)
    print(f"    Training samples: {X_train_scaled.shape[0]}")
    print(f"    Feature vector size: {X_train_scaled.shape[1]}")

    # ============================================================
    # 5. EXTRACT VALIDATION FEATURES
    # ============================================================
    print("\n[5] Extracting validation features (LBP + HOG)...")
    X_validation, y_validation = extractor.extract_features_batch(validation_records)
    X_validation_scaled = extractor.transform_features(X_validation)
    print(f"    Validation samples: {X_validation_scaled.shape[0]}")

    # ============================================================
    # 6. HYPERPARAMETER TUNING (Using Validation Set)
    # ============================================================
    print("\n[6] Hyperparameter tuning (using validation set)...")
    print("-" * 50)
    print("  C     Validation Accuracy")
    print("-" * 50)

    best_model = None
    best_C = None
    best_validation_accuracy = -1

    for C in C_VALUES:
        model = train_svm(X_train_scaled, y_train, C)
        validation_pred = model.predict(X_validation_scaled)
        validation_accuracy = accuracy_score(y_validation, validation_pred)

        print(f"  {C:>6}  {validation_accuracy:.4f}")

        if validation_accuracy > best_validation_accuracy:
            best_validation_accuracy = validation_accuracy
            best_C = C
            best_model = model

    print("-" * 50)
    print(f"Best C: {best_C}")
    print(f"Best validation accuracy: {best_validation_accuracy:.4f}")

    # ============================================================
    # 7. RETRAIN FINAL MODEL (Training + Validation)
    # ============================================================
    print("\n[7] Retraining final model (training + validation data)...")
    X_train_final = np.concatenate([X_train_scaled, X_validation_scaled])
    y_train_final = np.concatenate([y_train, y_validation])

    final_model = train_svm(X_train_final, y_train_final, best_C)

    # ============================================================
    # 8. SAVE MODEL
    # ============================================================
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    model_info = {
        "model": final_model,
        "best_C": best_C,
        "best_validation_accuracy": best_validation_accuracy,
        "lbp_num_points": LBP_POINTS,
        "lbp_radius": LBP_RADIUS,
        "hog_orientations": HOG_ORIENTATIONS,
        "feature_type": "LBP + HOG fusion"
    }

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model_info, f)

    print(f"\nFinal model saved to: {MODEL_PATH}")
    print("\n" + "=" * 70)
    print(" TRAINING COMPLETED SUCCESSFULLY")
    print("=" * 70)


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()

