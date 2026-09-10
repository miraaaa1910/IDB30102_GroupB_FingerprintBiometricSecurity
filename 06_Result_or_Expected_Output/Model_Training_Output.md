# Model Training Output

```text
======================================================================
 FINGERPRINT PUPPET ATTACK DETECTION
 LBP + HOG Fusion Features with SVM
======================================================================

[1] Loading dataset... 
    Total images: 5600

[2] Splitting dataset (70/10/20 at participant level)...
==============================
DATASET SPLIT
==============================
Training participants: 49
Validation participants: 7
Testing participants: 14

Training images: 3920
Validation images: 560
Testing images: 1120

[3] Creating LBP + HOG feature extractor...
[4] Extracting training features (LBP + HOG)...
    Training samples: 3920
    Feature vector size: 26270

[5] Extracting validation features (LBP + HOG)...
    Validation samples: 560

[6] Hyperparameter tuning (using validation set)...
--------------------------------------------------
  C     Validation Accuracy
--------------------------------------------------
   0.01  0.8571
   0.1   0.8929
   1.0   0.9107
  10.0   0.9107
 100.0   0.9107
--------------------------------------------------
Best C: 1.0
Best validation accuracy: 0.9107

[7] Retraining final model (training + validation data)...

Final model saved to: outputs/svm_lbp_hog_model.pkl
======================================================================
 TRAINING COMPLETED SUCCESSFULLY
======================================================================
