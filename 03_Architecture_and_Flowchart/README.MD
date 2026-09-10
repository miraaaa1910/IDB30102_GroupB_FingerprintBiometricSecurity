graph TD
    classDef moduleStyle fill:#b0c4de,stroke:#2b4c7e,stroke-width:2px,color:#000,font-weight:bold,align:left;

    subgraph System_Architecture ["3.4.1 System Architecture Diagram"]
        direction TD

        A["<b>DATA COLLECTION MODULE</b><br/><br/>1. Bonafide samples (Direct/ Angled/ Side)<br/>2. Simulated puppet attack samples (Direct/ Angled/ Side)<br/>3. Supporting datasets (LivDet2017/ 2019/ 2023)"]
        
        B["<b>PREPROCESSING MODULE</b><br/><br/>1. Image enhancement<br/>2. Noise removal<br/>3. Normalisation<br/>4. Segmentation"]
        
        C["<b>FEATURE EXTRACTION MODULE</b><br/><br/>1. LBP feature extraction<br/>2. HOG feature extraction<br/>3. Feature concatenation"]
        
        D["<b>CLASSIFICATION MODULE</b><br/><br/>1. Data splitting (70% training, 10% validation & 20% testing)<br/>2. SVM model training (RBF kernel)<br/>3. Hyperparameter optimisation (grid search)<br/>4. Model evaluation (accuracy, precision, recall, F1-score,<br/>ROC - AUC, APCER, BPCER, ACER)<br/>5. Output: Bonafide or simulated puppet attack"]

        A --> B
        B --> C
        C --> D
    end

    class A,B,C,D moduleStyle;
