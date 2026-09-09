# IDB30102_GroupB_FingerprintBiometricSecurity

## Research Title
Detecting Puppet Attacks in Fingerprint Authentication using Machine Learning

## Group Members
1. Amirah Zulaikha Binti Abdul Hadi 52215225002
2. Ainin Sofiya Binti Zamri 52215225029
3. Muhammad Nazir Bin Omar 52215226178
4. Muhammad Muzaffar Bin Abd Latif 52215226140
5. Muhammad Amirul Shazwan Bin Hawari 52215226195

## Assigned Research Area
## Research Problem
1. Limited research on puppet attack detection because most research focuses on traditional presentation attacks.
2. Limited datasets in terms of size and demographic diversity.
   
## Research Aim
To develop and evaluate a machine learning-based approach for detecting puppet attacks in fingerprint authentication systems, with the objective of improving the security and reliability of fingerprint-based authentication.

## Research Objectives
1. To develop a dataset containing genuine and puppet attack fingerprint samples for machine learning-based detection.
2. To develop a machine learning model for classifying genuine fingerprint samples and puppet attack samples.
3. To evaluate the performance of the developed machine learning model using appropriate evaluation metrics such as accuracy, precision, recall and F1-score.

## Proposed Solution
## Research Methodology & Development Model
## Evaluation Plan
## System Architecture
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
