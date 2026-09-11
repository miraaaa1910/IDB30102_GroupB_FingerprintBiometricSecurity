# 1. Proposed Architecture Diagram
```text

                      +-------------------------------------------------------------+
                      |                    DATA COLLECTION MODULE                   |
                      | 1. Bonafide samples (Direct / Angled / Side)                |
                      | 2. Simulated puppet attack samples (Direct / Angled / Side) |
                      | 3. Supporting datasets (LivDet2017 / 2019 / 2023)           |
                      +-------------------------------------------------------------+
                                                     |
                                                     v
                      +-------------------------------------------------------------+
                      |                    PREPROCESSING MODULE                     |
                      | 1. Image enhancement                                        |
                      | 2. Noise removal                                            |
                      | 3. Normalisation                                            |
                      | 4. Segmentation                                             |
                      +-------------------------------------------------------------+
                                                     |
                                                     v
                      +-------------------------------------------------------------+
                      |                  FEATURE EXTRACTION MODULE                  |
                      | 1. LBP feature extraction                                   |
                      | 2. HOG feature extraction                                   |
                      | 3. Feature concatenation                                    |
                      +-------------------------------------------------------------+
                                                     |
                                                     v
                      +-------------------------------------------------------------+
                      |                    CLASSIFICATION MODULE                    |
                      | 1. Data splitting (70% training, 10% validation & 20% test) |
                      | 2. SVM model training (RBF kernel)                          |
                      | 3. Hyperparameter optimisation (grid search)                |
                      | 4. Model evaluation (accuracy, precision, recall, F1-score, |
                      |    ROC-AUC, APCER, BPCER, ACER)                             |
                      | 5. Output: Bonafide or simulated puppet attack              |
                      +-------------------------------------------------------------+
```

Figure 1 shows the overall architecture of the proposed puppet attack detection system. The system consists of four main modules:

## 1. The Data Collection Module
   - Collects Bonafide fingerprint samples from participants placing their own fingers normally
   - Collects Simulated Puppet Attack samples with another participant assisting finger placement
   - Includes three pressing conditions: direct, angled, and side pressing
   - Integrates supporting LivDet2017, LivDet2019, and LivDet2023 datasets

## 2. The Preprocessing Module
- Applies image enhancement techniques such as histogram equalization and filtering
- Use Gaussian filtering to reduce image noise
- Normalizes fingerprint images to maintain consistent brightness and contrast
- Segments the fingerprint region from the background

## 3. The Feature Extraction Module
- Extracts LBP features to capture local texture patterns
- Extracts HOG features to capture edge and information
- Combines LBP and HOG features into a single feature vector for classification

## 4. The Classification Module.
- Splits the dataset into training (70%), validation (10%) and testing (20%)
- Trains a SVM classifier using RBF kernel
- Performs hyperparameter optimization using grid search with cross-validation
- Evaluates the model using multiple performance metrics

# 2. Research Proses flow Chart

```
                    +-------------------------------------------------------------+
                    |                            START                            |
                    +-------------------------------------------------------------+
                                                   |
                                                   v
                    +-------------------------------------------------------------+
                    |               PHASE 1 BUSINESS UNDERSTANDING                |
                    | 1. Define research problem                                  |
                    | 2. Define research objectives                               |
                    +-------------------------------------------------------------+
                                                   |
                                                   v
                    +-------------------------------------------------------------+
                    |                 PHASE 2: DATA UNDERSTANDING                 |
                    | 1. Identifying and collect data sources                     |
                    | 2. Explore and verify data quality                          |
                    +-------------------------------------------------------------+
                                                   |
                                                   v
                    +-------------------------------------------------------------+ <----+
                    |                  PHASE 3: DATA PREPARATION                  |      |
                    | 1. Preprocess fingerprint images                            |      |
                    | 2. Feature extraction                                       |      |
                    | 3. Data splitting                                           |      |
                    +-------------------------------------------------------------+      |
                                                   |                                     |
                                                   v                                     |
                    +-------------------------------------------------------------+ <+   |
                    |                      PHASE 4: MODELLING                     |  |   |
                    | 1. Model development                                        |  |   |
                    +-------------------------------------------------------------+  |   |
                                                   |                if poor performance  | If data issue
                                                   v                                 |   |
                    +-------------------------------------------------------------+  |   |
                    |                     PHASE 5: EVALUATION                     |--+   |
                    | 1. Model evaluation                                         |      |
                    +-------------------------------------------------------------+      |
                             |                                                           |
                             +-----------------------------------------------------------+
                                                   |
                                                   v
                    +-------------------------------------------------------------+
                    |               PHASE 6: DEPLOYMENT/ PROTOTYPE                |
                    | 1. Prototype development and documentation                  |
                    +-------------------------------------------------------------+
                                                   |
                                                   v
                    +-------------------------------------------------------------+
                    |                             END                             |
                   +-------------------------------------------------------------+
```

Figure 2 shows the proposed flow chart diagram. Below is a detailed explanation of each step in the research flow chart:

## 1. Define research problem
   - Identify puppet attacks as a security vulnerability in fingerprint authentication.
   - Recognise that conventional liveness detection may not detect puppet attacks because the fingerprint itself is genuine.
   - Establish the need for a machine learning-based detection approach.

## 2. Define research objectives
   - Develop a dataset containing Bonafide and Simulated Puppet Attack samples.
   - Develop a machine learning model to classify the fingerprint samples.
   - Evaluate the model performance using appropriate evaluation metrics.

## 3. Identify and collect data sources
   - Collect custom Bonafide samples using normal finger placement.
   - Collect custom Simulated Puppet Attack samples using assisted or forced finger placement.
   - Include three pressing conditions: direct, angled, and side pressing.
   - Include supporting PAD datasets from LivDet2017, LivDet2019, and LivDet2023.

## 4. Explore and verify data quality
   - Analyse the quality of the collected fingerprint images.
   - Check variations in fingerprint ridge patterns and image quality.
   - Check the balance between Bonafide and Simulated Puppet Attack classes.
   - Ensure sufficient participant diversity.

## 5. Preprocess fingerprint images
   - Apply histogram equalization to improve image contrast.
   - Apply Gaussian filtering to reduce sensor noise.
   - Normalize images to maintain consistent brightness and contrast.
   - Segment the fingerprint region from the background.

## 6. Feature extraction
   - Extract LBP features to capture local texture patterns using a radius of 1 and 8 neighbours.
   - Extract HOG features to capture edge and gradient information.
   - Combine the LBP and HOG features into a single feature vector.
   - Normalize the combined feature vectors for consistent scaling.

## 7. Data splitting
   - Divide the dataset into training (70%), validation (10%), and testing (20%) sets.
   - Ensure that samples from the same participant are kept within the same split to prevent data leakage.
   - Maintain a similar class distribution across the three sets.

## 8. Model development
   - Train an SVM classifier with an RBF kernel using the training set.
   - Perform grid search with 5-fold cross-validation to optimize the C and gamma parameters.
   - Use the validation set to assess the model during development and select the best-performing configuration.

## 9. Model evaluation
   - Evaluate the final model using the separate testing set.
   - Calculate classification metrics including Accuracy, Precision, Recall, F1-score, and ROC-AUC.
   - Calculate PAD-specific metrics including APCER, BPCER, and ACER.
   - Compare the obtained results with the expected performance of the baseline model.

## 10. Prototype development and documentation
- Develop a functional prototype to demonstrate the detection capability.
- Document the research methodology, results, limitations, and recommendations.
- Prepare the final research report.

# 3. Proposed Framework

1. **Business Understanding:** Defines the security threat posed by puppet attacks in fingerprint biometrics and sets target performance criteria for distinguishing genuine interaction from forced finger placement.
2. **Data Understanding:** Assesses dataset characteristics, image quality variations, and class distributions across custom collected samples and benchmark datasets (LivDet2017, LivDet2019, LivDet2023).
3. **Data Preparation:** Cleans and pre-processes fingerprint images through normalization, Gaussian filtering, histogram equalization, and ROI segmentation.
4. **Modeling:** Extracts LBP and HOG feature descriptors, concatenates them into unified feature vectors, and trains an Support Vector Machine (SVM) model using an RBF kernel.
5. **Evaluation:** Measures classifier robustness using standard classification metrics (Accuracy, Precision, Recall, F1-score, ROC-AUC) alongside biometric presentation attack detection metrics (APCER, BPCER, ACER).
6. **Deployment:** Documents the architectural pipeline and process execution flow for prototype verification and prospective system integration.

---

## Data Collection & Procedures

This research will use existing fingerprint datasets together with a small custom dataset. LivDet2017, LivDet2019 and LivDet2023 will be used as supporting fingerprint PAD data. However, Li et al. (2024) reported that existing datasets do not contain enough forced fingerprint samples for studying puppet attacks. Therefore, a custom dataset will be prepared based on the forced and unforced conditions used in their study.

Before data collection, ethics approval will be obtained from the relevant institutional committee. Participation will be voluntary, and participants will be provided with information about the study and asked to provide informed consent. Only the data required for the research will be collected, and participant information will be anonymised. Any personal data collected will be handled in accordance with the Personal Data Protection Act 2010 (PDPA).

The custom dataset will contain two proposed classes: Bonafide and Simulated Puppet Attack. These labels are adapted from the unforced and forced fingerprint conditions used by Li et al. (2024). Bonafide samples will be collected when participants place their own fingers normally, while simulated puppet-attack samples will involve another consenting participant assisting with the finger placement. Different pressing conditions, including direct, angled and side pressing, will be considered based on Li et al. (2024).

| Data Type | Sample Condition | Purpose |
| :--- | :--- | :--- |
| **Bonafide** | User places own finger normally | Normal authentication |
| **Simulated puppet attack** | Finger placed under forced conditions | Simulated puppet attack |
| **Existing dataset** | LivDet fingerprint samples | Supporting PAD data |

## Proposed Evaluation Plan

The proposed system will be treated as a binary classification problem, where the model predicts either Bonafide or Simulated Puppet Attack. An SVM will be used as the baseline model because Li et al. (2024) used SVM with LBP-HOG features to distinguish forced and unforced fingerprints. Their results showed that LBP-HOG with an SVM could effectively distinguish the two conditions.

The model will be evaluated using a separate test set. Accuracy, precision, recall, F1-score and ROC-AUC will be used to measure classification performance. APCER, BPCER and ACER will also be considered as PAD-specific metrics.

| Metric | Purpose |
| :--- | :--- |
| **Accuracy** | Measures the overall percentage of correct predictions |
| **Precision** | Measures how many detected attacks are actually attacks |
| **Recall** | Measures how many actual attacks are successfully detected |
| **F1-score** | Provides a balance between precision and recall |
| **ROC-AUC** | Measures the model's ability to separate the two classes |
| **APCER** | Measures the error of incorrectly accepting attack samples |
| **BPCER** | Measures the error of incorrectly rejecting bona fide samples |
| **ACER** | Provides the average of APCER and BPCER |



