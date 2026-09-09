# Model Evaluation Output

```text
======================================
MODEL EVALUATION
======================================

Loaded model with C = 1.0
Test images: 1120

Creating LBP + HOG feature extractor...
Extracting test features...

======================================
CONFUSION MATRIX
======================================
              Predicted
            Genuine  Puppet
Actual Genuine    512      48
Actual Puppet     52      508

======================================
STANDARD CLASSIFICATION METRICS
======================================
Accuracy : 0.9107
Precision: 0.9137
Recall   : 0.9071
F1-Score : 0.9104
ROC-AUC  : 0.9675

======================================
PAD-SPECIFIC METRICS
======================================
APCER (Attack Error)  : 0.0929
BPCER (Genuine Error) : 0.0857
ACER  (Average Error) : 0.0893

======================================
CLASSIFICATION REPORT
======================================
              precision    recall  f1-score   support

     Genuine     0.9078    0.9143    0.9110       560
     Puppet      0.9137    0.9071    0.9104       560

    accuracy                         0.9107      1120
   macro avg     0.9107    0.9107    0.9107      1120
weighted avg     0.9107    0.9107    0.9107      1120

Results saved to: outputs/evaluation_results.json
