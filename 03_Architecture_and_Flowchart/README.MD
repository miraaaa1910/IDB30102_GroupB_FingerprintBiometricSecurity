## 1. Proposed Architecture Diagram

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





 Fingures 1 shows the overall architecture of the proposed puppet attack detection system. The system consists of four main modules:

i.   The Data Collection Module
     - Collects Bonafide fingerprint samples from participants placing their own fingers normally
     - Collects Simulated Puppet Attack samples with another participant assisting finger placement
     - Includes three pressing conditions: direct, angled, and side pressing
     - Integrates supporting LivDet2017, LivDet2019, and LivDet2023 datasets

ii.  The Preprocessing Module
     - Applies image enhancement techniques such as histogram equalization and filtering
     - Use Gaussian filtering to reduce image noise
     - Normalizes fingerprint images to maintain consistent brightness and contrast
     - Segments the fingerprint region from the background

iii. The Feature Extraction Module
     - Extracts LBP features to capture local texture patterns
     - Extracts HOG features to capture edge and information
     - Combines LBP and HOG features into a single feature vector for classification

iv.  The Classification Module.
     - Splits the dataset into training (70%), validation (10%) and testing (20%)
     - Trains a SVM classifier using RBF kernel
     - Performs hyperparameter optimization using grid search with cross-validation
     - Evaluates the model using multiple performance metrics



                   2 System Flow chart
```text

                 2  Research Process Flow Chart

                                ( START )
                                    |
                                    v
            +-----------------------------------------------+
            |        PHASE 1: BUSINESS UNDERSTANDING        |
            |                                               |
            |           1. Define research problem          |
            |          2. Define research objectives        |
            +-----------------------+-----------------------+
                                    |
                                    v
            +-----------------------------------------------+
            |          PHASE 2: DATA UNDERSTANDING          |
            |                                               |
            |     1. Identifying and collect data sources   |
            |      2. Explore and verify data quality       |
            +-----------------------+-----------------------+
                                    |
                                    v
            +-----------------------------------------------+ <----+
            |            PHASE 3: DATA PREPARATION          |      |
            |                                               |      |
            |        1. Preprocess fingerprint images       |      |
            |              2. Feature extraction            |      |
            |                3. Data splitting              |      |
            +-----------------------+-----------------------+      |
                                    |                              |
                                    v                              |
            +-----------------------------------------------+ <+   |
            |               PHASE 4: MODELLING              |  |   | If data issue
            |                                               |  |   |
            |              1. Model development             |  |   |
            +-----------------------+-----------------------+  |   |
                                    |                          |   |
                                    v                          |   |
            +-----------------------------------------------+  |   |
            |               PHASE 5: EVALUATION             |  |   |
            |                                               |  |   |
            |               1. Model evaluation             |--+---+
            +-----------------------+-----------------------+  |
                                    |                          | If poor performance
                                    v                          +
            +-----------------------------------------------+
            |         PHASE 6: DEPLOYMENT/ PROTOTYPE        |
            |                                               |
            |         1. Prototype development and          |
            |                 documentation                 |
            +-----------------------+-----------------------+
                                    |
                                    v
                                 ( END )










