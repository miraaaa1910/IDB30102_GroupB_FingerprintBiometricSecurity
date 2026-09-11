# 3. Proposed Framework

1. **Business Understanding:** Defines the security threat posed by puppet attacks in fingerprint biometrics and sets target performance criteria for distinguishing genuine interaction from forced finger placement.
2. **Data Understanding:** Assesses dataset characteristics, image quality variations, and class distributions across custom collected samples and benchmark datasets (LivDet2017, LivDet2019, LivDet2023).
3. **Data Preparation:** Cleans and pre-processes fingerprint images through normalization, Gaussian filtering, histogram equalization, and ROI segmentation.
4. **Modeling:** Extracts LBP and HOG feature descriptors, concatenates them into unified feature vectors, and trains an Support Vector Machine (SVM) model using an RBF kernel.
5. **Evaluation:** Measures classifier robustness using standard classification metrics (Accuracy, Precision, Recall, F1-score, ROC-AUC) alongside biometric presentation attack detection metrics (APCER, BPCER, ACER).
6. **Deployment:** Documents the architectural pipeline and process execution flow for prototype verification and prospective system integration.

---

###  Data Collection & Procedures

This research will use existing fingerprint datasets together with a small custom dataset. LivDet2017, LivDet2019 and LivDet2023 will be used as supporting fingerprint PAD data. However, Li et al. (2024) reported that existing datasets do not contain enough forced fingerprint samples for studying puppet attacks. Therefore, a custom dataset will be prepared based on the forced and unforced conditions used in their study.

Before data collection, ethics approval will be obtained from the relevant institutional committee. Participation will be voluntary, and participants will be provided with information about the study and asked to provide informed consent. Only the data required for the research will be collected, and participant information will be anonymised. Any personal data collected will be handled in accordance with the Personal Data Protection Act 2010 (PDPA).

The custom dataset will contain two proposed classes: Bonafide and Simulated Puppet Attack. These labels are adapted from the unforced and forced fingerprint conditions used by Li et al. (2024). Bonafide samples will be collected when participants place their own fingers normally, while simulated puppet-attack samples will involve another consenting participant assisting with the finger placement. Different pressing conditions, including direct, angled and side pressing, will be considered based on Li et al. (2024).

| Data Type | Sample Condition | Purpose |
| :--- | :--- | :--- |
| **Bonafide** | User places own finger normally | Normal authentication |
| **Simulated puppet attack** | Finger placed under forced conditions | Simulated puppet attack |
| **Existing dataset** | LivDet fingerprint samples | Supporting PAD data |


