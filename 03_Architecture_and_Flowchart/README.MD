This directory contains the system architecture and process flow specifications for the proposed **Puppet Attack Detection System** in fingerprint authentication. All components strictly follow the methodology outlined in Section 3.4.1 of the research proposal.

---

## 1. System Architecture Diagram

```text
┌─────────────────────────────────────────────────────────────┐
│                   DATA COLLECTION MODULE                    │
│  1. Bonafide samples (Direct / Angled / Side)               │
│  2. Simulated puppet attack samples (Direct / Angled / Side)│
│  3. Supporting datasets (LivDet2017 / 2019 / 2023)          │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                    PREPROCESSING MODULE                     │
│  1. Image enhancement                                       │
│  2. Noise removal                                           │
│  3. Normalisation                                           │
│  4. Segmentation                                            │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                  FEATURE EXTRACTION MODULE                  │
│  1. LBP feature extraction                                  │
│  2. HOG feature extraction                                  │
│  3. Feature concatenation                                   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                     CLASSIFICATION MODULE                   │
│  1. Data splitting (70% training, 10% validation & 20% test)│
│  2. SVM model training (RBF kernel)                         │
│  3. Hyperparameter optimisation (grid search)               │
│  4. Model evaluation (accuracy, precision, recall, F1-score,│
│     ROC-AUC, APCER, BPCER, ACER)                            │
│  5. Output: Bonafide or simulated puppet attack             │
└─────────────────────────────────────────────────────────────┘
