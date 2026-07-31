# Clinical Data Dictionary — ASD Behavioral & Demographic Profiling

This document outlines the **34 columns** present in the processed dataset (`data/processed/Autism_Screening_Data_Processed.csv`).

---

## 📋 Feature Breakdown by Tier

| Column Name | Category | Description |
| :--- | :--- | :--- |
| `Patient_ID` | Identifier | Unique numerical index assigned to each patient record. |
| `A1` | Raw Behavioral Item | Eye contact when called by name (1 = Atypical/No, 0 = Typical/Yes). |
| `A2` | Raw Behavioral Item | Ease of others establishing eye contact with patient (1 = Atypical/No, 0 = Typical/Yes). |
| `A3` | Raw Behavioral Item | Pointing to request desired objects/wants (1 = Atypical/Absent, 0 = Typical/Present). |
| `A4` | Raw Behavioral Item | Pointing to share interesting items/events with others (1 = Atypical/Absent, 0 = Typical/Present). |
| `A5` | Raw Behavioral Item | Engagement in imaginative activities or role-play (1 = Atypical/Reduced, 0 = Typical/Active). |
| `A6` | Raw Behavioral Item | Following others' gaze to see what they are looking at (1 = Atypical/Reduced, 0 = Typical/Normal). |
| `A7` | Raw Behavioral Item | Attempting to comfort someone who appears upset (1 = Atypical/Absent, 0 = Typical/Active). |
| `A8` | Raw Behavioral Item | Communication style presentation (1 = Atypical/Non-standard, 0 = Typical/Standard). |
| `A9` | Raw Behavioral Item | Use of common body gestures like waving goodbye (1 = Atypical/Absent, 0 = Typical/Present). |
| `A10` | Raw Behavioral Item | Frequent staring into space without focus (1 = Atypical/Frequent, 0 = Typical/Rare). |
| `Sex` | Demographics | Gender of the individual (`Male`, `Female`). |
| `Age` | Demographics | Age of individual in years (treated with IQR Winsorization for biological outliers). |
| `Age_Group` | Demographics | Age categorization (`Child`, `Adolescent`, `Adult`). |
| `Generational_Cohort` | Demographics | Generational cohort mapping (`Gen Alpha (Child)`, `Gen Z`, `Millennial`, `Gen X`, `Boomer`). |
| `Jaundice` | Medical History | Indicates if born with neonatal jaundice (1 = Yes, 0 = No). |
| `Family_ASD` | Genetic Background | Indicates if an immediate family member has ASD (1 = Yes, 0 = No). |
| `Risk_Overlap` | Medical History | Combination string of pre-existing background risk factors (Jaundice, Family ASD). |
| `High_Risk_Background` | Medical History | Derived binary indicator of elevated congenital/familial background risk. |
| `Total_Atypical_Trait_Burden` | Macro Severity Score | Global severity score equal to the sum of atypical items A1 through A10 (0 - 10 scale). |
| `Social_Interaction_Score` | Domain Sub-Score | Sum of social interaction deficits (`A1` + `A2` + `A6`, range 0 - 3). |
| `Communication_Deficit_Score` | Domain Sub-Score | Sum of functional communication deficits derived from `A3`, `A4`, `A9` (range 0 - 3). |
| `Behavioral_Atypicality_Score` | Domain Sub-Score | Sum of behavioral & imagination atypicalities derived from `A5`, `A7`, `A8`, `A10` (range 0 - 4). |
| `Social_Comm_Imbalance_Profile` | Micro Variance | Categorical profile identifying asymmetry between social motivation and communication ability. |
| `Eye_Contact_Discordance` | Micro Variance | Measures discrepancy between name-call eye contact and general eye contact ease (highlights potential masking). |
| `Empathy_Imagination_Profile` | Micro Variance | Category combining empathy (`A7`) and imagination (`A5`) trait presentations. |
| `Genetic_Severity_Matrix` | Micro Variance | Matrix cross-evaluating familial genetic history against trait severity burden. |
| `Diagnostic_Proximity_Band` | Clinical Banding | Tri-level band classification (`Clear Negative` [0-3], `Borderline / Monitor` [4-6], `Clinical Range` [7-10]). |
| `Behavioral_Archetype` | Clinical Cluster | Qualitative cluster (`Communication Impaired`, `Socially Withdrawn`, `Severe Global Delay`, `Mild/Typical Presentation`, `Highly Atypical Presentation`). |
| `Class` | Screening Outcome | Ground-truth screening diagnostic class (`Yes` = Potential ASD, `No` = Typical). |
| `Late_Diagnosis_Flag` | Healthcare Proxy | Flag for individuals screened/diagnosed at an older age relative to cohort. |
| `Masking_Proxy_Flag` | Healthcare Proxy | Indicator suggesting potential symptom masking. |
| `Sub_Clinical_Missed_Flag` | Healthcare Proxy | Flag identifying potentially missed sub-clinical cases. |
| `Compensatory_Masking_Flag` | Healthcare Proxy | Algorithmic proxy isolating older individuals (Age 13+) with high trait burden (5+) but 0 social interaction deficit (`High Masking Potential` vs `Standard`). |
