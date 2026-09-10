┌────────────────────────────────────────────────────────────────────────┐
│                        DATA COLLECTION MODULE                          │
│                                                                        │
│  1. Bonafide Samples (Direct, Angled, Side)                            │
│  2. Simulated Puppet Attack Samples (Direct, Angled, Side)             │
│  3. Supporting Datasets (LivDet2017 / LivDet2019 / LivDet2023)         │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                         PREPROCESSING MODULE                           │
│                                                                        │
│  1. Image Enhancement (Histogram Equalization)                         │
│  2. Noise Removal (Gaussian Filtering)                                 │
│  3. Normalisation                                                      │
│  4. Segmentation (Foreground Extraction)                               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                      FEATURE EXTRACTION MODULE                         │
│                                                                        │
│  1. LBP Feature Extraction (Local Texture)                             │
│  2. HOG Feature Extraction (Edges / Gradients)                         │
│  3. Feature Concatenation (Unified Vector)                             │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        CLASSIFICATION MODULE                           │
│                                                                        │
│  1. Data Splitting (70% Training, 10% Validation, 20% Testing)         │
│  2. SVM Model Training (RBF Kernel)                                    │
│  3. Hyperparameter Optimisation (Grid Search)                          │
│  4. Model Evaluation (Accuracy, Precision, Recall, F1, ROC-AUC,        │
│                        APCER, BPCER, ACER)                             │
│  5. Output Classification: [ Bonafide ] or [ Simulated Puppet Attack ] │
└────────────────────────────────────────────────────────────────────────┘


## Proposed System Architecture

![Proposed System Architecture](system_architecture.png)

### Description
The proposed system architecture consists of four integrated modules designed to detect puppet attacks in fingerprint authentication:
1. **Data Collection Module:** Captures Bonafide and Simulated Puppet Attack samples under three pressing conditions (Direct, Angled, Side), alongside supporting LivDet benchmark datasets.
2. **Preprocessing Module:** Performs image quality enhancement, Gaussian noise reduction, intensity normalization, and fingerprint region segmentation.
3. **Feature Extraction Module:** Extracts Local Binary Pattern (LBP) texture features and Histogram of Oriented Gradients (HOG) descriptors, concatenating them into a unified feature vector.
4. **Classification Module:** Partitions data (70/10/20 split), trains a Support Vector Machine (SVM) classifier with an RBF kernel, optimizes hyperparameters via grid search, and outputs the final prediction (*Bonafide* vs. *Simulated Puppet Attack*) along with performance metrics.
