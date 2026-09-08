## 1. Literature Review Analysis Table

| Theme | Key Studies | Methods / Algorithms | Key Findings | Limitations |
|---|---|---|---|---|
| **Soft Computing & Multimodal Biometrics** | Hussain et al. (2025); Rajakumar & Shanthi (2025); Chitrapu et al. (2026); Houssein et al. (2023) | CNN-LSTM, Multimodal CNN, Adaptive Focal Loss, Homomorphic Encryption | Achieved approximately **98–100% accuracy**; multimodal biometrics improves detection and authentication robustness | Adds system complexity; cross-sensor compatibility issues; privacy concerns |
| **Unsupervised & Deep Learning for Anti-Spoofing** | Zhang et al. (2023); Kothadiya et al. (2023); Yook et al. (2024); Adami et al. (2024); Li & Ramachandra (2025) | ResNet, Transformer, Autoencoder, Attention Mechanism | Deep learning dominates Presentation Attack Detection (PAD); unsupervised learning can detect previously unseen attacks | Generalisation to unseen attacks remains challenging |
| **Systematic Reviews & Emerging Challenges** | Ametefe et al. (2024); Casula et al. (2024); Herke (2026); Li & Ramachandra (2025) | Literature Review, Comparative Analysis | No single universal algorithm performs best across all attack types; puppet attacks remain underexplored | Most studies lack extensive real-world validation |

---

## 2. Comparison of Existing Techniques

| Approach | Examples | Advantages | Disadvantages |
|---|---|---|---|
| **Traditional Handcrafted Features** | LBP, HOG, GLDS | Simple and lightweight; low computational requirements | Poor generalisation to unseen attacks |
| **Deep Learning** | CNN, ResNet, Transformer | Learns complex patterns automatically; generally achieves high accuracy | Requires large training datasets; computationally expensive |
| **Unsupervised Learning** | Autoencoder | Can detect unseen attacks without requiring spoof samples during training | Limited training data; cross-sensor compatibility issues |
| **Multimodal Biometrics** | Face + Fingerprint | Improves accuracy, reliability, and robustness | Adds system complexity; privacy concerns |
| **Lightweight Models** | MobileNetV2, LFLDNet | Suitable for edge and resource-constrained devices | May sacrifice some detection accuracy |

---

## 3. Research Gap Analysis

| No. | Research Gap | Evidence | Implication |
|---|---|---|---|
| **1** | **Limited research specifically on puppet attacks** | Most fingerprint spoofing studies focus on fake materials such as silicone, gelatin, and latex. Puppet attacks receive less attention because the attack uses a genuine fingerprint from a live user. Li et al. (2024) introduced a Puppet Attack Dataset and achieved detection rates of **78.1%–97.2%**, but detection performance decreased significantly for angled and side pressing. | More research is needed to specifically investigate puppet attacks and distinguish voluntary and involuntary fingerprint authentication using genuine fingerprints. |
| **2** | **Limited availability of puppet attack datasets** | Li et al. (2024) introduced a Puppet Attack Dataset containing **5,600 images from 70 volunteers**. However, the dataset has limited demographic diversity and does not sufficiently represent different user populations and attack conditions. | More diverse and representative puppet attack datasets are required to improve the reliability and generalisation of machine learning models. |
| **3** | **Variations in puppet attack conditions** | Existing studies mainly investigate straight pressing conditions. Li et al. (2024) reported a detection rate of **97.2% for straight pressing**, which decreased to **86.5% for angled pressing** and **78.1% for side pressing**. | Future models should consider different pressing angles, finger positions, and attack behaviours to improve robustness in real-world conditions. |

---

## 4. Summary of Methods and Algorithms

| Method / Algorithm | Study | Application |
|---|---|---|
| **CNN-LSTM** | Hussain et al. (2025) | Fingerprint authentication |
| **Multimodal CNN + Adaptive Focal Loss** | Rajakumar & Shanthi (2025) | Fingerprint liveness detection |
| **MobileNetV2 + TAF + CKKS** | Chitrapu et al. (2026) | Multimodal face-fingerprint authentication |
| **LFLDNet (ResNet + Transformer)** | Zhang et al. (2023) | Lightweight fingerprint liveness detection |
| **Sequential Attention + ResNet** | Kothadiya et al. (2023) | Fingerprint Presentation Attack Detection (PAD) |
| **Unsupervised Autoencoder + CBAM** | Adami et al. (2024) | Detection of unseen fingerprint attacks |
| **LBP-HOG + SVM** | Li et al. (2024) | Puppet attack detection |

---

## 5. Relevant Datasets

| Dataset | Year / Version | Main Purpose | Relevance |
|---|---|---|---|
| **LivDet** | 2017, 2019, 2023 | Fingerprint liveness detection benchmark | Evaluation of Presentation Attack Detection (PAD) |
| **FVC** | 2000, 2002, 2004 | Fingerprint verification competition | Fingerprint recognition and authentication |
| **Puppet Attack Dataset** | 2024 | Puppet attack detection | Directly relevant to puppet attack detection |
| **CASIA-FingerV5** | - | Multimodal face-fingerprint biometric dataset | Multimodal biometric research |
| **SOCOFing** | - | Fingerprint dataset | Fingerprint recognition and classification |

---

## 6. Evaluation Metrics

| Metric | Description | Application |
|---|---|---|
| **Accuracy** | Measures the overall proportion of correctly classified samples | General classification performance |
| **Precision** | Measures the proportion of predicted positive samples that are actually positive | Classification performance |
| **Recall** | Measures the proportion of actual positive samples correctly identified | Sensitivity / attack detection |
| **F1-Score** | Harmonic mean of precision and recall | Balanced classification evaluation |
| **EER** | Equal Error Rate where FAR and FRR are equal | Biometric authentication |
| **FAR** | False Acceptance Rate | Authentication systems |
| **FRR** | False Rejection Rate | Authentication systems |
| **APCER** | Attack Presentation Classification Error Rate | Presentation Attack Detection |
| **BPCER** | Bona Fide Presentation Classification Error Rate | Presentation Attack Detection |
| **ACER** | Average Classification Error Rate, commonly calculated from APCER and BPCER | Overall PAD performance |

---

## 7. References Supporting the Proposed Methodology

1. Zhang, K., Huang, S., Liu, E., & Zhao, H. (2023). *LFLDNet: Lightweight fingerprint liveness detection based on ResNet and transformer*. Sensors, 23(15), 7842.

2. Hussain, A., Murshed, F., Alandoli, M. N., & Aljafari, G. (2025). *A hybrid deep learning approach for secure biometric authentication using fingerprint data*. Computers, 14(5), 178.

3. Li, G., Ma, Y., Wang, W., Zhang, J., & Luo, H. (2024). *The self-detection method of the puppet attack in biometric fingerprinting*. IEEE Internet of Things Journal, 11(10).

4. Ametefe, D. S., et al. (2024). *Enhancing fingerprint authentication: A systematic review of liveness detection methods against presentation attacks*. Journal of The Institution of Engineers (India): Series B, 105(5).

5. Yook, H. J., et al. (2024). *Attention map is all we need for lightweight fingerprint liveness detection*. IEEE Access, 12.

6. Santos, N., Ghita, B., & Masala, G. L. (2024). *Medical systems data security and biometric authentication in public cloud servers*. IEEE Transactions on Emerging Topics in Computing, 12(2), 572–582.

7. Adami, B., Hosseinzadehketilateh, M. R., & Karimian, N. (2024). *Contactless fingerprint biometric anti-spoofing: An unsupervised deep learning approach*. 2024 IEEE International Joint Conference on Biometrics (IJCB).
