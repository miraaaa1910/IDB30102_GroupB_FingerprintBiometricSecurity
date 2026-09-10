3.4.1 System Architecture Diagram
Figure 1 Proposed System Architecture for Puppet Attack Detection
23
Figure 1 shows the overall architecture of the proposed puppet attack detection system. The system consists of four main modules:
i. The Data Collection Module
- Collects Bonafide fingerprint samples from participants placing their own fingers normally
- Collects Simulated Puppet Attack samples with another participant assisting finger placement
- Includes three pressing conditions: direct, angled, and side pressing
- Integrates supporting LivDet2017, LivDet2019, and LivDet2023 datasets
ii. The Preprocessing Module
- Applies image enhancement techniques such as histogram equalization and filtering
- Use Gaussian filtering to reduce image noise
- Normalizes fingerprint images to maintain consistent brightness and contrast
- Segments the fingerprint region from the background
iii. The Feature Extraction Module
- Extracts LBP features to capture local texture patterns
- Extracts HOG features to capture edge and information
