# Jet Suppression Analysis

This repository contains Python and C++ code developed to analyze path-length dependent jet suppression in Pb-Pb collisions using the JEWEL event generator.

## Repository Structure

### 1. /data_processing_files
This folder contains the core pipeline for transforming raw simulation output into analyzable data. The scripts should be run in the following sequence:
* Afterburn.py: Initial filtering (applying p_T, eta, and centrality cuts).
* combined_events.py: Merges separate 3000 and 1000 event profiles into a unified dataset.
* final_event_processing.py: Calculates initial-state geometry, specifically participant plane angles (Psi_2) and eccentricity (epsilon).
* final_events.py: The final compilation script that aggregates all variables into the primary analysis files.
* final_state_particles.py: A utility script for identifying and mapping PDG IDs of final state particles.

### 2. /data_analysis_files
Contains the scripts used to perform the analysis of the processed data. 

### 3. /final_state_main_data_files
This directory acts as the storage for the individual histogram data. The file PbPb.extra.3000 is quite large and has been uploaded to Google Drive. 
It can be accessed via the following link:
https://drive.google.com/file/d/1OGn0ZrtBS7ceUJbwjiFwY9by6rc41p90/view?usp=sharing

### 4. /txt_files
A dedicated output directory for the .txt files generated. 

## Execution Flow
1. Ensure all raw .afterburned simulation files are present in the local directory.
2. Run the scripts within /data_processing_files in the order listed above.
3. The resulting datasets will be saved automatically to the /txt_files folder for analysis.

## Academic Reference
This code was developed as part of a Bachelor’s Thesis at Lund University.
* Simulation Tool: JEWEL (Jet Evolution With Energy Loss)
* Objective: To qualitatively reproduce ALICE collaboration results regarding the path-length dependence of jet quenching.
