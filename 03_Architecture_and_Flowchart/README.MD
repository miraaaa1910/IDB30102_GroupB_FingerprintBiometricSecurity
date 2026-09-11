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


Figure 2 shows the proposed flow chart diagram. Below is a detailed explanation of each step in the research flow chart:

1. **Define research problem**
   - Identify puppet attacks as a security vulnerability in fingerprint authentication.
   - Recognise that conventional liveness detection may not detect puppet attacks because the fingerprint itself is genuine.
   - Establish the need for a machine learning-based detection approach.

2. **Define research objectives**
   - Develop a dataset containing Bonafide and Simulated Puppet Attack samples.
   - Develop a machine learning model to classify the fingerprint samples.
   - Evaluate the model performance using appropriate evaluation metrics.

3. **Identify and collect data sources**
   - Collect custom Bonafide samples using normal finger placement.
   - Collect custom Simulated Puppet Attack samples using assisted or forced finger placement.
   - Include three pressing conditions: direct, angled, and side pressing.
   - Include supporting PAD datasets from LivDet2017, LivDet2019, and LivDet2023.

4. **Explore and verify data quality**
   - Analyse the quality of the collected fingerprint images.
   - Check variations in fingerprint ridge patterns and image quality.
   - Check the balance between Bonafide and Simulated Puppet Attack classes.
   - Ensure sufficient participant diversity.

5. **Preprocess fingerprint images**
   - Apply histogram equalization to improve image contrast.
   - Apply Gaussian filtering to reduce sensor noise.
   - Normalize images to maintain consistent brightness and contrast.
   - Segment the fingerprint region from the background.

6. **Feature extraction**
   - Extract LBP features to capture local texture patterns using a radius of 1 and 8 neighbours.
   - Extract HOG features to capture edge and gradient information.
   - Combine the LBP and HOG features into a single feature vector.
   - Normalize the combined feature vectors for consistent scaling.

7. **Data splitting**
   - Divide the dataset into training (70%), validation (10%), and testing (20%) sets.
   - Ensure that samples from the same participant are kept within the same split to prevent data leakage.
   - Maintain a similar class distribution across the three sets.

8. **Model development**
   - Train an SVM classifier with an RBF kernel using the training set.
   - Perform grid search with 5-fold cross-validation to optimize the C and gamma parameters.
   - Use the validation set to assess the model during development and select the best-performing configuration.

9. **Model evaluation**
   - Evaluate the final model using the separate testing set.
   - Calculate classification metrics including Accuracy, Precision, Recall, F1-score, and ROC-AUC.
   - Calculate PAD-specific metrics including APCER, BPCER, and ACER.
   - Compare the obtained results with the expected performance of the baseline model.

10. **Prototype development and documentation**
    - Develop a functional prototype to demonstrate the detection capability.
    - Document the research methodology, results, limitations, and recommendations.
    - Prepare the final research report.
