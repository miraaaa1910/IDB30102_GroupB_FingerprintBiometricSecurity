# **DATA OR SAMPLE INPUT**

## Sources and Links

- **Paper DOI**: 10.1109/JIOT.2024.3365714
- **Official GitHub repository**: [https://github.com/Lynnon/The-Self-Detection-Method-of-the-Puppet-Attack-in-Biometric-Fingerprinting](https://github.com/Lynnon/The-Self-Detection-Method-of-the-Puppet-Attack-in-Biometric-Fingerprinting)
- **LivDet Competition portal**: [http://livdet.org/](http://livdet.org/)

## Content

### [Sample Dataset](sample_dataset.md)
Details the two primary datasets—the capacitive Puppet Attack Dataset (5,600 samples from 70 subjects across Scenarios S1–S4) and the LivDet 2017 Presentation Attack Detection (PAD) benchmark covering optical and thermal modalities.

### [Sample Image](sample_images)
Defines the required image specifications, including resolutions (160 × 160 px for the BM2166 sensor; 500 × 500, 252 × 324, and 300 × n px for LivDet scanners), color depths, and PDPA-compliant handling.

### [Sample Input Format](sample_input_format.md)
Provides the standardized file manifest schema to pair relative image paths and acquisition scenarios with binary classification labels (`0` for Bonafide, `1` for Attack).

### [Sample Sensor Data](sample_sensor_data.md)
Outlines the sensor hardware profiles and operational environments, including the BM2166 module paired with the STM32F407ZET6 microcontroller, as well as Green Bit, Digital Persona, and Orcanthus scanner parameters
