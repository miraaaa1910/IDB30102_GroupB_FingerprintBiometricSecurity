flowchart TD
    classDef phase fill:#2b2d42,stroke:#8d99ae,stroke-width:2px,color:#fff;

    P1["<b>Phase 1: Business Understanding</b><br/>Define research problem & formulate objectives"] ::: phase
    
    P2["<b>Phase 2: Data Understanding</b><br/>Identify, collect, explore, and verify Bonafide &<br/>Simulated Puppet Attack data across pressing angles"] ::: phase
    
    P3["<b>Phase 3: Data Preparation</b><br/>Image preprocessing, LBP + HOG feature extraction,<br/>& train/validation/test split with subject separation"] ::: phase
    
    P4["<b>Phase 4: Modelling</b><br/>Train & tune RBF-SVM classifier using training<br/>and validation sets"] ::: phase
    
    P5["<b>Phase 5: Evaluation</b><br/>Assess final model performance on test set using<br/>standard & PAD-specific metrics"] ::: phase
    
    P6["<b>Phase 6: Deployment / Prototype</b><br/>Develop functional prototype to demonstrate real-time<br/>puppet attack detection & complete documentation"] ::: phase

    P1 --> P2
    P2 --> P3
    P3 --> P4
    P4 -- "If poor performance<br/>(re-tune model)" --> P4
    P4 --> P5
    P5 -- "If data/feature issues<br/>(re-preprocess & engineer)" --> P3
    P5 --> P6
