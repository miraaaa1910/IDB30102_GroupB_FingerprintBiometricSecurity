import numpy as np
import cv2
from skimage.feature import local_binary_pattern, hog
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

class PuppetAttackDetectionSystem:
    def __init__(self):
        # SVM setup with RBF kernel as specified in Section 3.4.1
        self.svm_model = None
        self.best_params = None

    # =========================================================================
    # MODULE 2: PREPROCESSING MODULE
    # =========================================================================
    def preprocess_image(self, image_path, target_size=(128, 128)):
        """
        Executes Section 3.4.1 Preprocessing Pipeline:
        1. Image Enhancement
        2. Noise Removal
        3. Normalisation
        4. Segmentation
        """
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise FileNotFoundError(f"Could not read image from {image_path}")

        # 1. Image Enhancement (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced_img = clahe.apply(img)

        # 2. Noise Removal (Gaussian Blur)
        denoised_img = cv2.GaussianBlur(enhanced_img, (3, 3), 0)

        # 3. Normalisation (Scale intensity values to [0, 1])
        normalised_img = cv2.normalize(denoised_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

        # 4. Segmentation (Otsu Thresholding to separate foreground fingerprint area)
        resized_img = cv2.resize(normalised_img, target_size, interpolation=cv2.INTER_AREA)
        _, segmented_img = cv2.threshold(resized_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Mask original normalized image with segmentation mask
        masked_fingerprint = cv2.bitwise_and(resized_img, resized_img, mask=segmented_img)
        
        return masked_fingerprint

    # =========================================================================
    # MODULE 3: FEATURE EXTRACTION MODULE
    # =========================================================================
    def extract_lbp_features(self, image, radius=1, n_points=8):
        """1. LBP feature extraction"""
        lbp = local_binary_pattern(image, P=n_points, R=radius, method="uniform")
        n_bins = n_points + 2
        hist, _ = np.histogram(lbp.ravel(), bins=n_bins, range=(0, n_bins), density=True)
        return hist

    def extract_hog_features(self, image):
        """2. HOG feature extraction"""
        hog_features = hog(
            image,
            orientations=9,
            pixels_per_cell=(8, 8),
            cells_per_block=(2, 2),
            block_norm='L2-Hys',
            transform_sqrt=True
        )
        return hog_features

    def extract_features(self, image):
        """
        3. Feature concatenation
        Combines LBP and HOG feature vectors into a single vector.
        """
        lbp_feats = self.extract_lbp_features(image)
        hog_feats = self.extract_hog_features(image)
        concatenated_vector = np.hstack([lbp_feats, hog_feats])
        return concatenated_vector

    # =========================================================================
    # MODULE 4: CLASSIFICATION MODULE
    # =========================================================================
    def train_and_optimize(self, X, y):
        """
        1. Data splitting (70% training, 10% validation, 20% testing)
        2. SVM model training (RBF kernel)
        3. Hyperparameter optimisation (Grid search)
        """
        # Step 1: Split 80% train+val, 20% testing
        X_train_val, X_test, y_train_val, y_test = train_test_split(
            X, y, test_size=0.20, random_state=42, stratify=y
        )
        
        # Split remaining 80% into 70% overall train and 10% overall validation (10/80 = 0.125)
        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=0.125, random_state=42, stratify=y_train_val
        )

        print(f"Dataset Split Completed:")
        print(f" - Train Samples: {len(X_train)} (70%)")
        print(f" - Validation Samples: {len(X_val)} (10%)")
        print(f" - Test Samples: {len(X_test)} (20%)")

        # Step 2 & 3: SVM RBF Kernel Training & Hyperparameter Optimization
        param_grid = {
            'C': [0.1, 1, 10, 100],
            'gamma': ['scale', 'auto', 0.01, 0.001]
        }
        
        base_svm = SVC(kernel='rbf', probability=True, random_state=42)
        
        print("\nExecuting Grid Search Hyperparameter Optimisation...")
        grid_search = GridSearchCV(base_svm, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
        grid_search.fit(X_train, y_train)
        
        self.svm_model = grid_search.best_estimator_
        self.best_params = grid_search.best_params_
        print(f"Optimal Hyperparameters: {self.best_params}")

        # Validate Model
        val_acc = self.svm_model.score(X_val, y_val)
        print(f"Validation Set Accuracy: {val_acc * 100:.2f}%")

        return X_test, y_test

    def evaluate_metrics(self, X_test, y_test):
        """
        4. Model evaluation (accuracy, precision, recall, F1-score, ROC-AUC, APCER, BPCER, ACER)
        5. Output: Bonafide or simulated puppet attack
        """
        y_pred = self.svm_model.predict(X_test)
        y_probs = self.svm_model.predict_proba(X_test)[:, 1]

        # Standard Machine Learning Metrics
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_probs)

        # Biometric Anti-Spoofing Metrics (APCER, BPCER, ACER)
        # Confusion Matrix: TN (Bonafide correctly classified), FP (Bonafide misclassified as Attack)
        # FN (Attack misclassified as Bonafide), TP (Attack correctly classified)
        cm = confusion_matrix(y_test, y_pred)
        tn, fp, fn, tp = cm.ravel()

        apcer = fn / (fn + tp) if (fn + tp) > 0 else 0.0  # Attack Presentation Classification Error Rate
        bpcer = fp / (fp + tn) if (fp + tn) > 0 else 0.0  # Bonafide Presentation Classification Error Rate
        acer = (apcer + bpcer) / 2.0                    # Average Classification Error Rate

        print("\n================ SYSTEM EVALUATION METRICS ================")
        print(f"Accuracy : {acc * 100:.2f}%")
        print(f"Precision: {prec * 100:.2f}%")
        print(f"Recall   : {rec * 100:.2f}%")
        print(f"F1-Score : {f1 * 100:.2f}%")
        print(f"ROC-AUC  : {roc_auc:.4f}")
        print("-----------------------------------------------------------")
        print(f"APCER    : {apcer * 100:.2f}% (Attack Presentation Classification Error Rate)")
        print(f"BPCER    : {bpcer * 100:.2f}% (Bonafide Presentation Classification Error Rate)")
        print(f"ACER     : {acer * 100:.2f}% (Average Classification Error Rate)")
        print("===========================================================\n")

    def predict_sample(self, feature_vector):
        """Output classification: 0 = Bonafide, 1 = Simulated Puppet Attack"""
        prediction = self.svm_model.predict([feature_vector])[0]
        label = "Simulated Puppet Attack" if prediction == 1 else "Bonafide"
        return label


# =========================================================================
# DEMONSTRATION PIPELINE
# =========================================================================
if __name__ == "__main__":
    system = PuppetAttackDetectionSystem()

    print("Generating simulated data aligned with LivDet / Custom Dataset structure...")
    num_samples = 200
    dummy_features = []
    
    # Simulating features vectors generated from Module 3
    for _ in range(num_samples):
        # Dummy concatenated LBP (10) + HOG (1764) features
        dummy_vector = np.random.rand(1774)
        dummy_features.append(dummy_vector)
        
    X = np.array(dummy_features)
    # Binary targets: 0 = Bonafide, 1 = Puppet Attack
    y = np.random.choice([0, 1], size=num_samples, p=[0.5, 0.5])

    # Train model through Module 4 pipeline
    X_test, y_test = system.train_and_optimize(X, y)

    # Evaluate using metrics specified in Module 4
    system.evaluate_metrics(X_test, y_test)
