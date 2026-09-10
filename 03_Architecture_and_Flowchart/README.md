# 6. Architecture and System Flow – 03_Architecture_and_Flowchart/

## Proposed System Architecture

The proposed system architecture for detecting puppet attacks consists of four integrated processing modules:

1. **Data Collection Module:** Captures Bonafide samples (Direct, Angled, Side), Simulated Puppet Attack samples (Direct, Angled, Side), and supporting PAD benchmark datasets (LivDet2017, LivDet2019, LivDet2023).[cite: 2]
2. **Preprocessing Module:** Handles image quality enhancement via histogram equalization, noise reduction using Gaussian filtering, intensity normalization, and foreground fingerprint region segmentation.[cite: 2]
3. **Feature Extraction Module:** Extracts Local Binary Pattern (LBP) texture features and Histogram of Oriented Gradients (HOG) edge/gradient descriptors, followed by feature concatenation into a single unified feature vector.[cite: 2]
4. **Classification Module:** Performs data partitioning (70% training, 10% validation, 20% testing), trains a Support Vector Machine (SVM) classifier with an RBF kernel, optimizes hyperparameters using grid search, and outputs the final classification (*Bonafide* or *Simulated Puppet Attack*) alongside key performance metrics.[cite: 2]
