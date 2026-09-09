import numpy as np
from skimage import feature
from sklearn.preprocessing import StandardScaler
from preprocessing import preprocess_image

# ============================================================
# LOCAL BINARY PATTERNS
# ============================================================

class LocalBinaryPatterns:
    def __init__(self, num_points=24, radius=8):
        self.num_points = num_points
        self.radius = radius
    
    def describe(self, image, eps=1e-7):
        """Extract Local Binary Pattern features."""
        # Compute LBP representation
        lbp = feature.local_binary_pattern(
            image,
            self.num_points,
            self.radius,
            method="uniform"
        )
        
        # Build histogram
        histogram, _ = np.histogram(
            lbp.ravel(),
            bins=np.arange(0, self.num_points + 3),
            range=(0, self.num_points + 2)
        )
        
        # Normalize histogram
        histogram = histogram.astype("float")
        histogram /= (histogram.sum() + eps)
        
        return histogram


# ============================================================
# HISTOGRAM OF ORIENTED GRADIENTS
# ============================================================

class HistogramOfOrientedGradients:
    def __init__(self, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2)):
        self.orientations = orientations
        self.pixels_per_cell = pixels_per_cell
        self.cells_per_block = cells_per_block
    
    def describe(self, image):
        """Extract HOG features."""
        features = feature.hog(
            image,
            orientations=self.orientations,
            pixels_per_cell=self.pixels_per_cell,
            cells_per_block=self.cells_per_block,
            visualize=False,
            feature_vector=True
        )
        return features


# ============================================================
# FEATURE EXTRACTOR (LBP + HOG FUSION)
# ============================================================

class FeatureExtractor:
    """
    Combines LBP and HOG features into a single feature vector.
    Reference: Li et al. (2024) - LBP-HOG fusion feature
    """
    
    def __init__(self, lbp_points=24, lbp_radius=8, hog_orientations=9):
        self.lbp = LocalBinaryPatterns(num_points=lbp_points, radius=lbp_radius)
        self.hog = HistogramOfOrientedGradients(orientations=hog_orientations)
        self.scaler = StandardScaler()
        self.is_fitted = False
    
    def extract_features_from_image(self, image_path):
        """
        Extract combined LBP + HOG features from a single image.
        """
        # Preprocess image
        processed_image = preprocess_image(image_path)
        
        # Extract LBP
        lbp_features = self.lbp.describe(processed_image)
        
        # Extract HOG
        hog_features = self.hog.describe(processed_image)
        
        # Fuse features by concatenation
        combined_features = np.concatenate([lbp_features, hog_features])
        
        return combined_features
    
    def extract_features_batch(self, records):
        """
        Extract combined features from multiple image records.
        
        Args:
            records: List of dictionaries with 'path' and 'label' keys
        
        Returns:
            X: Feature matrix (n_samples, n_features)
            y: Labels (n_samples,)
        """
        X = []
        y = []
        
        for record in records:
            try:
                features = self.extract_features_from_image(record["path"])
                X.append(features)
                y.append(record["label"])
            except Exception as e:
                print(f"Error processing: {record['path']}")
                print(e)
        
        X = np.array(X)
        y = np.array(y)
        
        return X, y
    
    def fit_scaler(self, X_train):
        """Fit the scaler on training features."""
        self.scaler.fit(X_train)
        self.is_fitted = True
    
    def transform_features(self, X):
        """Transform features using fitted scaler."""
        if not self.is_fitted:
            raise ValueError("Scaler not fitted. Call fit_scaler() first.")
        return self.scaler.transform(X)
    
    def fit_transform(self, X_train):
        """Fit scaler and transform training features."""
        self.fit_scaler(X_train)
        return self.transform_features(X_train)


# ============================================================
# LEGACY FUNCTION (for backward compatibility)
# ============================================================

def extract_dataset_features(records, descriptor=None):
    """
    Legacy function for backward compatibility.
    Now uses the FeatureExtractor class.
    """
    extractor = FeatureExtractor()
    X, y = extractor.extract_features_batch(records)
    return X, y


# ============================================================
# MAIN TEST
# ============================================================

if __name__ == "__main__":
    print("Feature extraction module loaded successfully.")
    print("Using LBP + HOG fusion as per Li et al. (2024)")
    
    extractor = FeatureExtractor()
    
    cells_per_side = 224 // 8  # = 28
    blocks_per_side = cells_per_side - 2 + 1  # = 27
    hog_features = blocks_per_side * blocks_per_side * 2 * 2 * 9  # = 26,244
    
    # LBP features: num_points + 2 = 26
    lbp_features = 26
    total_features = lbp_features + hog_features
    
    print(f"LBP Parameters: points=24, radius=8")
    print(f"HOG Parameters: orientations=9, cells=(8,8), blocks=(2,2)")
    print(f"LBP features: {lbp_features}")
    print(f"HOG features: {hog_features}")
    print(f"Combined feature vector size: {total_features}")
