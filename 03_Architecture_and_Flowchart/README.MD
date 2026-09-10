import os
import cv2
import numpy as np
from skimage.feature import local_binary_pattern, hog
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

class PuppetAttackDetector:
    """
    Implements the 4-module architecture for Puppet Attack Detection:
    1. Data Collection / Loading
    2. Preprocessing
    3. Feature Extraction (LBP + HOG)
    4. Classification (SVM)
    """

    def __init__(self, lbp_radius=1, lbp_n_points=8):
        self.lbp_radius = lbp_radius
        self.lbp_n_points = lbp_n_points
        self.classifier = SVC(kernel='linear', C=1.0, random_state=42)

    def preprocess_image(self, image_path, target_size=(128, 128)):
        """
        Module 2: Preprocessing
        Converts image to grayscale and resizes to target dimensions.
        """
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"Image not found at path: {image_path}")
        
        # Convert to Grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Resize image
        resized = cv2.resize(gray, target_size, interpolation=cv2.INTER_AREA)
        return resized

    def extract_lbp_features(self, image):
        """
        Extracts Local Binary Patterns (LBP) histogram features.
        """
        lbp = local_binary_pattern(
            image, 
            P=self.lbp_n_points, 
            R=self.lbp_radius, 
            method="uniform"
        )
        # Compute normalized histogram
        n_bins = self.lbp_n_points + 2
        hist, _ = np.histogram(lbp.ravel(), bins=n_bins, range=(0, n_bins), density=True)
        return hist

    def extract_hog_features(self, image):
        """
        Extracts Histogram of Oriented Gradients (HOG) features.
        """
        features = hog(
            image,
            orientations=9,
            pixels_per_cell=(8, 8),
            cells_per_block=(2, 2),
            transform_sqrt=True,
            block_norm='L2-Hys'
        )
        return features

    def extract_features(self, image):
        """
        Module 3: Feature Extraction
        Concatenates LBP and HOG feature vectors.
        """
        lbp_feat = self.extract_lbp_features(image)
        hog_feat = self.extract_hog_features(image)
        
        # Fusion of feature vectors
        combined_features = np.hstack([lbp_feat, hog_feat])
        return combined_features

    def train(self, X_train, y_train):
        """
        Module 4: Training the Classification Model (SVM)
        """
        self.classifier.fit(X_train, y_train)

    def predict(self, X_test):
        """
        Module 4: Classification Prediction
        0 = Bonafide, 1 = Puppet Attack
        """
        return self.classifier.predict(X_test)


# --- Example Usage / CRISP-DM Process Flow Pipeline ---
if __name__ == "__main__":
    detector = PuppetAttackDetector()

    # Step 1: Simulate Sample Synthetic Data
    # (Replace this section with your actual image dataset loader)
    print("[CRISP-DM Phase: Data Preparation] Loading and extracting features...")
    
    num_samples = 100
    dummy_images = np.random.randint(0, 256, (num_samples, 128, 128), dtype=np.uint8)
    dummy_labels = np.random.randint(0, 2, num_samples) # 0: Bonafide, 1: Puppet Attack

    # Step 2: Feature Extraction Pipeline
    X = []
    for img in dummy_images:
        features = detector.extract_features(img)
        X.append(features)
    X = np.array(X)

    # Step 3: Train / Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, dummy_labels, test_size=0.2, random_state=42
    )

    # Step 4: Model Training
    print("[CRISP-DM Phase: Modelling] Training SVM Classifier...")
    detector.train(X_train, y_train)

    # Step 5: Model Evaluation
    print("[CRISP-DM Phase: Evaluation] Evaluating Classifier...")
    predictions = detector.predict(X_test)
    
    print("\nAccuracy Score:", accuracy_score(y_test, predictions))
    print("\nClassification Report:\n", classification_report(y_test, predictions, target_names=["Bonafide", "Puppet Attack"]))
