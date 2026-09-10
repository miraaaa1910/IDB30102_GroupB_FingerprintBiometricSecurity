# Architecture and System Flow

This folder contains the system architecture diagrams, process flowcharts, and technical schemas developed for the fingerprint biometric security project.

## Diagram Files

| File / Diagram | Description |
| :--- | :--- |
| **system_architecture.png** | Illustrates the high-level system architecture, showing interactions between the fingerprint sensor, processing unit, database, and user interface. |
| **process_flowchart.png** | Maps the step-by-step logic workflow from fingerprint capture and feature extraction to matching and authentication. |
| **data_flow_diagram.png** | Outlines how data moves through various processing stages (preprocessing, feature fusion, and classification). |

## System Workflow

The architectural pipeline follows this sequence:

Fingerprint Capture 
  ↓
Image Preprocessing (ROI Segmentation & Normalization)
  ↓
Feature Extraction (LBP & HOG Fusion)
  ↓
Model Matching / PAD Verification
  ↓
Authentication Result (Access Granted / Denied)
