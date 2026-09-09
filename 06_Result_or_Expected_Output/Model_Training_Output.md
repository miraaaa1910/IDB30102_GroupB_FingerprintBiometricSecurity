# Fingerprint Puppet Attack Detection
## LBP + HOG Fusion Features with SVM

### 1. Dataset Loading

- **Total images:** 5,600

### 2. Dataset Splitting

The dataset was split into **70/10/20** for training, validation, and testing at the participant level.

| Dataset | Participants | Images |
|---|---:|---:|
| Training | 49 | 3,920 |
| Validation | 7 | 560 |
| Testing | 14 | 1,120 |
| **Total** | **70** | **5,600** |

### 3. Feature Extraction

The model uses a combination of **Local Binary Pattern (LBP)** and **Histogram of Oriented Gradients (HOG)** features.

- **Feature extractor:** LBP + HOG
- **Training samples:** 3,920
- **Feature vector size:** 26,270
- **Validation samples:** 560

### 4. Hyperparameter Tuning

The SVM model was tested with different values of **C** using the validation dataset.

| C | Validation Accuracy |
|---:|---:|
| 0.01 | 0.8571 |
| 0.1 | 0.8929 |
| 1.0 | **0.9107** |
| 10.0 | 0.9107 |
| 100.0 | 0.9107 |

**Best C:** 1.0  
**Best Validation Accuracy:** 0.9107

### 5. Final Model Training

After selecting the best hyperparameter, the final SVM model was retrained using the **training and validation datasets**.

**Model output:**

```text
outputs/svm_lbp_hog_model.pkl
