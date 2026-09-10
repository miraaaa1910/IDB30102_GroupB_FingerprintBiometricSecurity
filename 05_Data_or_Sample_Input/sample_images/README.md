# Sample Images Specification

## Privacy Notice
Due to privacy restrictions under the Personal Data Protection Act 2010 (PDPA) and the ethical clearance agreement (IEC for Clinical Research Application No. 2023ZDSYLL109-Y01), raw participant fingerprint images are not publicly hosted in this repository.

## Image Properties & Format
The machine learning pipeline expects fingerprint images matching the physical extraction specifications defined by Li et al. (2024):

* **File Format:** Grayscale Bitmap (`.bmp`) or Lossless Portable Network Graphics (`.png`)
* **Resolution:** 160 × 160 pixels
* **Color Depth:** 8-bit single-channel grayscale (pixel values 0–255)
* **Spatial Resolution:** 508 DPI
* **Active Sensing Area:** 8.0 mm × 8.0 mm
* **Acquisition Device:** BM2166 Capacitive Fingerprint Module

## Sample File Naming Convention
* Bona Fide: `subject_[ID]_normal_[sample_num].bmp`
* Simulated Puppet Attack (Straight): `subject_[ID]_forced_straight_[sample_num].bmp`
* Simulated Puppet Attack (Angled): `subject_[ID]_forced_angled_[sample_num].bmp`
* Simulated Puppet Attack (Side): `subject_[ID]_forced_side_[sample_num].bmp`
