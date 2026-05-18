# Data Processing: Heavy-Ion Jet Suppression Analysis

This repository contains the Python scripts used to process and analyze event data for the Bachelor's thesis. The python scripts filter raw event output, calculates geometric properties, and prepares the final datasets for jet suppression evaluation.

## Execution Flow

To reproduce the final dataset, the scripts should be executed in the following order:

1. Afterburn.py
   - Purpose   : Initial data cleaning filtering.
   - Functions : Applies cuts for transverse momentum (p_T), pseudo-rapidity (eta), and event centrality to the raw data given in final_state_main_data_files.
   - Output    : event_numbers_more_3000.txt, txt_files/event_numbers_more_1000.txt

2. combined_events.py
   - Purpose   : Dataset merging.
   - Functions : Combines the processed event profiles from the 3000-event and 1000-event runs into one file.
   - Output    : combined_events.txt

3. final_event_processing.py
   - Purpose   : Geometric and shape analysis.
   - Functions : Calculates initial-state properties from Trajectum, specifically extracting the eccentricity (epsilon_2) and the participant plane angle (Psi_2).
   - Output    : combined_id_eps_phi.txt


4. final_events.py
   - Purpose   : Final data compilation.
   - Functions : Sets all calculated variables into a single output file.
   - Output    : final_events.txt

## Utility Scripts

* final_state_particles.py
  - Purpose    : Particle Identification (PID).
  - Description: This script maps the PDG (Particle Data Group) IDs of the final state particles. It is used to identify the specific hadron species produced after fragmentation and medium   interaction.

## Output Directory
All processed text outputs are stored in the /txt_files directory for use in the final evaluation plotting scripts.
