# Overview
This folder contains the Python source code developed for the fingerprint puppet attack detection system. The implementation uses image preprocessing, LBP and HOG feature fusion, and a Linear Support Vector Machine (SVM) classifier.

## Source Code Files

| File | Description |
|---|---|
| `data_loader.py` | Loads fingerprint images, extracts labels and participant IDs, and performs participant-level dataset splitting. |
| `preprocessing.py` | Performs grayscale conversion, histogram equalization, Gaussian filtering, ROI segmentation, image resizing, and pixel normalization. |
| `feature_extraction.py` | Extracts Local Binary Pattern (LBP) and Histogram of Oriented Gradients (HOG) features and combines them into a single feature vector. |
| `model_training.py` | Extracts features, applies feature scaling, trains Linear SVM models, selects the best C value using validation data, and saves the final model and scaler. |
| `model_evaluation.py` | Evaluates the trained model using standard classification metrics and Presentation Attack Detection (PAD) metrics. |

## Processing Pipeline

The implemented system follows the following workflow:

```text
Fingerprint Images
        ↓
Data Loading
        ↓
Participant-Level Dataset Split
70% Training / 10% Validation / 20% Testing
        ↓
Image Preprocessing
        ↓
Grayscale Conversion
        ↓
Histogram Equalization
        ↓
Gaussian Filtering
        ↓
ROI Segmentation
        ↓
Image Resizing (224 × 224)
        ↓
Pixel Normalization
        ↓
LBP + HOG Feature Extraction
        ↓
StandardScaler
        ↓
Linear SVM
        ↓
Validation-Based C Selection
        ↓
Final Training using Training + Validation Data
        ↓
Model Evaluation using Test Data

````
## Dataset Structure

```text
dataset/
├── Genuine/
│   ├── P001/
│   ├── P002/
│   └── ...
└── Puppet/
    ├── P001/
    ├── P002/
    └── ...
````
The dataset is split at the participant level:

- Training: 70%
- Validation: 10%
- Testing: 20%

This prevents the same participant from appearing in different splits.

## Method
````text
Fingerprint Images
        ↓
Preprocessing
        ↓
LBP + HOG Feature Extraction
        ↓
StandardScaler
        ↓
Linear SVM
        ↓
Model Evaluation
````
## Requirements
- Python 3
- NumPy
- OpenCV
- scikit-image
- scikit-learn

Install the required libraries:

````
pip install numpy opencv-python scikit-image scikit-learn
````
## How to Run
1. Load and split the dataset
````
python data_loader.py
````
2. Train the model
````
python model_training.py
````
3. Evaluate the model
````
python model_evaluation.py
````

### Outputs

The following files will be generated in the outputs/ folder:

````
outputs/
├── dataset_splits.json
├── svm_lbp_hog_model.pkl
└── evaluation_results.json
````

The evaluation includes:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- APCER
- BPCER
- ACER
- Confusion Matrix
