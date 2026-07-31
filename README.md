# 🧬 Beyond the Diagnosis: Clinical Profiling & Analytics

![Python](https://img.shields.io/badge/Python-3.10%2B-2C6975?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40%2B-68B2A0?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-CDE0C9?style=for-the-badge&labelColor=2C6975&color=68B2A0)
![Methodology](https://img.shields.io/badge/Methodology-Deterministic_Scoring-2C6975?style=for-the-badge)

An end-to-end clinical data science framework and interactive web platform that analyzes Autism Spectrum Disorder (ASD) screening traits across **6,075 patients**.

Instead of defaulting to opaque "black-box" machine learning classifiers, this project focuses entirely on **deep clinical phenotyping, a 7-tier feature engineering architecture, demographic profiling, and inferential hypothesis testing**.

---

## 🎯 Executive Summary & Core Objectives

Traditional screening models often reduce complex behavioral presentations to a binary classification flag ($1$ or $0$). This project transitions raw questionnaire data into an explainable behavioral spectrum:

1. **7-Tier Feature Engineering**: Expands 10 raw survey responses into 3 domain sub-scores (*Social Interaction*, *Communication Deficits*, *Behavioral Atypicality*), 5 behavioral archetypes, and clinical proximity bands.
2. **Identifying the "Sub-Clinical Bubble"**: Isolates **1,717 patients (28.3%)** sitting just below diagnostic thresholds who require preventative monitoring.
3. **Algorithmic Camouflage Detection**: Flags **475 patients (Age 13+)** exhibiting high global trait burdens while scoring 0 on social interaction deficits—isolating social masking/camouflaging.
4. **Inferential Statistical Validation**:
   * **Chi-Square Test ($p = 0.0036$)**: Proves gender significantly alters diagnostic presentation rates.
   * **Mann-Whitney U Test ($p < 0.0001$)**: Statistically validates that engineered trait scores separate clinical populations.
   * **Familial Odds Ratio ($1.77\times$)**: Proves an immediate family history of ASD inflates screening odds by 77%.

---

## 🖥️ Live Web Application Features (`app.py`)

The repository includes a modern, high-contrast web application built with Streamlit and Plotly, styled in a custom clinical palette (`#2C6975`, `#68B2A0`, `#CDE0C9`, `#E0ECDE`, `#FFFFFF`):

* **📊 Executive Clinical Summary**: High-level KPI cards, cohort breakdown charts, and core methodology highlights.
* **📖 Data Dictionary & Interactive Explorer**: Searchable 34-column feature dictionary with dynamic dataset filtering and 1-click CSV exporting.
* **🩺 Patient Trait & Masking Calculator**: Interactive $A1–A10$ clinical intake form that real-time calculates domain scores, diagnostic bands, and masking flags (*100% deterministic rule-based, no ML*).
* **🔬 Behavioral Phenotyping & EDA**: Interactive Plotly bar, pie, and box charts with live filter findings updated dynamically.
* **⚖️ Inferential Statistical Proofs**: Hypothesis test visualizer detailing Chi-Square, Mann-Whitney U, and Odds Ratio results.

---

## 📁 Repository Structure

```
.
├── app.py                  # Main Streamlit web application
├── header_icon.jpg         # Custom 3D clinical header branding icon
├── requirements.txt        # Python dependencies for deployment
├── README.md               # GitHub repository documentation
├── .gitignore              # Configured Git exclusions
├── .streamlit/
│   └── config.toml         # Custom Streamlit theme configuration
├── data/
│   ├── raw/                # Baseline raw screening dataset (6,075 records)
│   └── processed/          # Feature-engineered dataset (34 columns)
├── notebooks/
│   └── Autism_Spectral_Disorder.ipynb # End-to-end data analytics & statistical notebook
├── dashboard/
│   └── Insight_Igniters_dashboard.pbix # Power BI interactive dashboard
└── docs/
    ├── DATA_DICTIONARY.md  # 34-column data dictionary documentation
    └── ASD Data Analytics_ Feature Engineering, Visualizations, and Statistical Framework.pdf
```

---

## 🚀 Quickstart & Local Installation

### Prerequisites
* Python 3.10 or higher
* Git

### Step-by-Step Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   cd YOUR_REPOSITORY
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   Open `http://localhost:8501` in your browser.

---

## 🌐 Deploy Live to Streamlit Community Cloud (Free)

1. Push this repository to GitHub.
2. Sign in to **[share.streamlit.io](https://share.streamlit.io/)** with GitHub.
3. Click **New App** $\rightarrow$ Select your repository.
4. Set Main file path: `app.py`.
5. Click **Deploy**! 🎈

---

## 📜 License

This project is open-source under the **MIT License**.
