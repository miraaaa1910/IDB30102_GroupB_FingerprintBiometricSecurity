# IDB30102_GroupB_FingerprintBiometricSecurity

## Research Title
Detecting Puppet Attacks in Fingerprint Authentication using Machine Learning

## Group Members
1. Amirah Zulaikha Binti Abdul Hadi 52215225002
2. Ainin Sofiya Binti Zamri 52215225029
3. Muhammad Nazir Bin Omar 52215226178
4. Muhammad Muzaffar Bin Abd Latif 52215226140
5. Muhammad Amirul Shazwan Bin Hawari 52215226195

## Research Problem
1. Limited research on puppet attack detection because most research focuses on traditional presentation attacks.
2. Limited datasets in terms of size and demographic diversity.
   
## Research Aim
To develop and evaluate a machine learning-based approach for detecting puppet attacks in fingerprint authentication systems with the objective of improving the security and reliability of fingerprint-based authentication.

## Research Objectives
1. To develop a dataset containing genuine and puppet attack fingerprint samples for machine learning-based detection.
2. To develop a machine learning model for classifying genuine fingerprint samples and puppet attack samples.
3. To evaluate the performance of the developed machine learning model using appropriate evaluation metrics such as  accuracy, precision, recall, F1-score, ROC-AUC, APCER, BPCER and ACER.

## Proposed Solution
* A machine learning-based approach is proposed to detect puppet attacks in fingerprint authentication systems
* The solution targets security threats where a legitimate user is coerced to authenticate using their genuine fingerprint
* It utilizes a Support Vector Machine (SVM) classifier combined with Local Binary Patterns (LBP) and Histogram of Oriented Gradients (HOG) feature extraction
* The approach evaluates fingerprint samples across direct, angled and side pressing conditions

## Research Methodology & Development Model
* The study adopts a quantitative experimental research design
* It follows the 6-phase Cross-Industry Standard Process for Data Mining (CRISP-DM) model
* Business Understanding defines the research problem, objectives and security risks of puppet attacks
* Data Understanding identifies and collects bonafide samples, simulated puppet attacks and supporting LivDet datasets
* Data Preparation cleans, normalizes, segments fingerprint images and extracts LBP and HOG features
* Modelling involves selecting, training and optimizing an SVM classifier to differentiate normal authentication from puppet attacks
* Evaluation assesses model performance using classification and PAD metrics
* Deployment/Prototype demonstrates the detection mechanism as an additional security layer for fingerprint authentication

## Evaluation Plan
* The detection model is treated as a binary classification problem predicting either Bonafide or Simulated Puppet Attack
* Evaluation is performed using a separate test set
* Standard classification metrics include accuracy, precision, recall, F1-score, and ROC-AUC
* PAD-specific metrics include APCER, BPCER and ACER to measure error rates

## System Architecture
* **Data Collection Module**: Gathers bonafide samples, simulated puppet attack samples across direct, angled, and side pressing conditions, and LivDet datasets
* **Preprocessing Module**: Performs image enhancement, Gaussian noise removal, normalization, and background segmentation
* **Feature Extraction Module**: Extracts LBP local texture features and HOG edge/gradient features, combining them into a unified feature vector
* **Classification Module**: Splits data into 70% training, 10% validation, and 20% testing sets, trains an SVM classifier with an RBF kernel via grid search optimization, and outputs the final classification

## Technical Component
| Item | Details |
|---|---|
| Programming language | Python |
| IDE / Editor	| Visual Studio Code	|
|Version Control	|Git & GitHub |
|Image Processing	|OpenCV |
|Feature Extraction	|scikit-image |
| Machine Learning	|scikit-learn |
|Numerical Processing|	NumPy	|
|Data Serialization	|Python Pickle / JSON	|
|Dataset	|Fingerprint dataset containing Genuine and Puppet attack samples |
|Machine Learning Model|	Linear Support Vector Machine (LinearSVC) |
|Development Environment|Python 3.x|

## Mapping Technical Work to Research Objectives
|Research Objectives| Supporting Component | GitHub Location |
|---|---|---|
|RO1| To develop a dataset containing genuine and puppet attack fingerprint samples for machine learning-based detection. |  05_Data_or_Sample_Input/ |
|RO2| To develop a machine learning model for classifying genuine fingerprint samples and puppet attack samples.| 03_Architecture_and_Flowchart/ and 04_Source_Code/ |
|RO3| To evaluate the performance of the developed machine learning model using appropriate evaluation metrics such as  accuracy, precision, recall, F1-score, ROC-AUC, APCER, BPCER, and ACER. | 06_Results_or_Expected_Output/|

## Instruction for Executing Preliminary Code
1. Install Python 3.x on the computer.
2. Install the required libraries:
   ````
   pip install numpy opencv-python scikit-image scikit-learn
   ````
3. Place the fingerprint dataset inside the dataset/ folder using the required structure:
   ````
   dataset/
   ├── Genuine/
   │   ├── P001/
   │   └── P002/
   └── Puppet/
    ├── P001/
    └── P002/
   ````

4. Run the data loader to split the dataset:
   ````
   python data_loader.py
5. Run the model training:
   ````
   python model_training.py
6. Run the evaluation code:
   ````
   python model_evaluation.py

The trained model and evaluation results will be saved in the outputs/ folder.
