@startuml
skinparam rectangle {
    BackgroundColor #B0C4DE
    BorderColor #2B4C7E
    FontColor #000000
}

rectangle "<b>DATA COLLECTION MODULE</b>\n\n1. Bonafide samples (Direct/ Angled/ Side)\n2. Simulated puppet attack samples (Direct/ Angled/ Side)\n3. Supporting datasets (LivDet2017/ 2019/ 2023)" as Module1

rectangle "<b>PREPROCESSING MODULE</b>\n\n1. Image enhancement\n2. Noise removal\n3. Normalisation\n4. Segmentation" as Module2

rectangle "<b>FEATURE EXTRACTION MODULE</b>\n\n1. LBP feature extraction\n2. HOG feature extraction\n3. Feature concatenation" as Module3

rectangle "<b>CLASSIFICATION MODULE</b>\n\n1. Data splitting (70% training, 10% validation & 20% testing)\n2. SVM model training (RBF kernel)\n3. Hyperparameter optimisation (grid search)\n4. Model evaluation (accuracy, precision, recall, F1-score, ROC-AUC, APCER, BPCER, ACER)\n5. Output: Bonafide or simulated puppet attack" as Module4

Module1 --> Module2
Module2 --> Module3
Module3 --> Module4
@enduml
