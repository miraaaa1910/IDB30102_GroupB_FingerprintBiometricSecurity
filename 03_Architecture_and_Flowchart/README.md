# Architecture and System Flow

This folder contains the system architecture diagrams, process flowcharts, and technical schemas developed for the fingerprint biometric security project.

## Diagram Files

| File / Diagram | Description |
| :--- | :--- |
| **system_architecture.png** | Illustrates the high-level system architecture across four integrated modules: Data Collection, Preprocessing, Feature Extraction, and Classification. |
| **process_flowchart.png** | Maps the step-by-step methodology and experimental pipeline based on the CRISP-DM framework. |
| **data_flow_diagram.png** | Outlines how raw fingerprint images move through preprocessing, feature fusion (LBP + HOG), and SVM classification. |

---

1 Proposed System Architecture

The proposed system architecture for detecting puppet attacks consists of four integrated processing modules:

1. **Data Collection Module:** Captures Bonafide samples (Direct, Angled, Side), Simulated Puppet Attack samples (Direct, Angled, Side), and supporting PAD benchmark datasets (LivDet2017, LivDet2019, LivDet2023).
   
3. **Preprocessing Module:** Handles image quality enhancement via histogram equalization, noise reduction using Gaussian filtering, intensity normalization, and foreground fingerprint region segmentation.
   
5. **Feature Extraction Module:** Extracts Local Binary Pattern (LBP) texture features and Histogram of Oriented Gradients (HOG) edge/gradient descriptors, followed by feature concatenation into a single unified feature vector.

7. **Classification Module:** Performs data partitioning (70% training, 10% validation, 20% testing), trains a Support Vector Machine (SVM) classifier with an RBF kernel, optimizes hyperparameters using grid search, and outputs the final classification (*Bonafide* or *Simulated Puppet Attack*) alongside key performance metrics.

---

