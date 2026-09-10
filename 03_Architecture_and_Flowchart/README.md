# Architecture and System Flow

This folder contains the system architecture diagrams, process flowcharts, and technical schemas developed for the fingerprint biometric security project.

## Diagram Files

| File / Diagram | Description |
| :--- | :--- |
| **system_architecture.png** | Illustrates the high-level system architecture across four integrated modules: Data Collection, Preprocessing, Feature Extraction, and Classification. |
| **process_flowchart.png** | Maps the step-by-step methodology and experimental pipeline based on the CRISP-DM framework. |
| **data_flow_diagram.png** | Outlines how raw fingerprint images move through preprocessing, feature fusion (LBP + HOG), and SVM classification. |

---

## Proposed System Architecture

The proposed system architecture for detecting puppet attacks consists of four integrated processing modules:

1. **Data Collection Module:** Captures Bonafide samples (Direct, Angled, Side), Simulated Puppet Attack samples (Direct, Angled, Side), and supporting PAD benchmark datasets (LivDet2017, LivDet2019, LivDet2023).
2. **Preprocessing Module:** Handles image quality enhancement via histogram equalization, noise reduction using Gaussian filtering, intensity normalization, and foreground fingerprint region segmentation.
3. **Feature Extraction Module:** Extracts Local Binary Pattern (LBP) texture features and Histogram of Oriented Gradients (HOG) edge/gradient descriptors, followed by feature concatenation into a single unified feature vector.
4. **Classification Module:** Performs data partitioning (70% training, 10% validation, 20% testing), trains a Support Vector Machine (SVM) classifier with an RBF kernel, optimizes hyperparameters using grid search, and outputs the final classification (*Bonafide* or *Simulated Puppet Attack*) alongside key performance metrics.

---

## Process Flow (CRISP-DM Lifecycle)

The operational process flow adheres to the 6 phases of the CRISP-DM methodology:

1. **Phase 1: Business Understanding:** Define the research problem (vulnerability to forced/coerced authentications) and formulate objectives.
2. **Phase 2: Data Understanding:** Identify, collect, explore, and verify the quality of collected Bonafide and Simulated Puppet Attack data across different pressing angles.
3. **Phase 3: Data Preparation:** Perform image preprocessing, LBP + HOG feature extraction, and split the data into training, validation, and testing sets while preserving subject separation.
4. **Phase 4: Modelling:** Train and tune the RBF-SVM classifier using training and validation sets. *(If poor performance is observed during validation, return to Phase 4 for model re-tuning).*
5. **Phase 5: Evaluation:** Assess final model performance on the test set using standard and PAD-specific metrics. *(If data/feature issues are discovered, return to Phase 3 for re-preprocessing and feature engineering).*
6. **Phase 6: Deployment / Prototype:** Develop a functional prototype to demonstrate real-time puppet attack detection capability and complete documentation.

---

## System Workflow & Data Stages

The architectural pipeline moves through four sequential stages:
