import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
try:
    from scipy import stats
except ImportError:
    stats = None
import os

# -----------------------------------------------------------------------------
# Page Configuration & Styling
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Insight Igniters - ASD Clinical Analytics",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for polished clinical dashboard aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #0F172A;
    }
    .metric-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .metric-title {
        color: #94A3B8;
        font-size: 0.875rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .metric-value {
        color: #F8FAFC;
        font-size: 1.875rem;
        font-weight: 700;
        margin-top: 4px;
    }
    .metric-subtitle {
        color: #38BDF8;
        font-size: 0.8rem;
        margin-top: 4px;
    }
    .badge-clinical {
        background-color: #EF4444;
        color: white;
        padding: 4px 12px;
        border-radius: 9999px;
        font-weight: 600;
    }
    .badge-borderline {
        background-color: #F59E0B;
        color: white;
        padding: 4px 12px;
        border-radius: 9999px;
        font-weight: 600;
    }
    .badge-negative {
        background-color: #10B981;
        color: white;
        padding: 4px 12px;
        border-radius: 9999px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Data Loading & Caching
# -----------------------------------------------------------------------------
@st.cache_data
def load_processed_data():
    csv_path = os.path.join(os.path.dirname(__file__), "data", "processed", "Autism_Screening_Data_Processed.csv")
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    else:
        st.error(f"Processed dataset not found at path: {csv_path}")
        return pd.DataFrame()

df = load_processed_data()

# -----------------------------------------------------------------------------
# Sidebar Navigation
# -----------------------------------------------------------------------------
st.sidebar.image("https://img.icons8.com/isometric-folders/100/brain.png", width=70)
st.sidebar.title("Insight Igniters")
st.sidebar.caption("Beyond the Diagnosis: Clinical Profiling & Analytics")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation Menu",
    [
        "📊 Executive Clinical Summary",
        "🩺 Patient Intake & Trait Calculator",
        "🔬 Behavioral Phenotyping & EDA",
        "⚖️ Inferential Statistical Proofs",
        "🚀 Live Cloud Deployment Guide"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Methodology Guarantee**\n"
    "This platform relies strictly on deterministic feature engineering, "
    "clinical sub-domain scoring, and inferential statistics. It contains "
    "**no black-box Machine Learning prediction models**."
)

# -----------------------------------------------------------------------------
# PAGE 1: EXECUTIVE CLINICAL SUMMARY
# -----------------------------------------------------------------------------
if menu == "📊 Executive Clinical Summary":
    st.title("📊 Beyond the Diagnosis: Executive Clinical Summary")
    st.markdown(
        "Standard autism screening frameworks often default to binary predictive classification. "
        "This platform delivers **deep clinical phenotyping, 7-tier feature architecture, and inferential statistics** "
        "across **6,075 screening records**."
    )
    st.markdown("---")

    # High Level Metric Cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">Total Cohort</div>
                <div class="metric-value">6,075</div>
                <div class="metric-subtitle">Screened Patients</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        borderline_count = len(df[df['Diagnostic_Proximity_Band'] == 'Borderline / Monitor']) if not df.empty else 1717
        borderline_pct = (borderline_count / len(df) * 100) if not df.empty else 28.3
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Borderline / Monitor</div>
                <div class="metric-value">{borderline_count:,}</div>
                <div class="metric-subtitle">{borderline_pct:.1f}% Sub-Clinical Bubble</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        masking_count = len(df[df['Compensatory_Masking_Flag'] == 'High Masking Potential']) if not df.empty else 475
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Compensatory Masking</div>
                <div class="metric-value">{masking_count}</div>
                <div class="metric-subtitle">Camouflaging Patients Identified</div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">Familial Risk Impact</div>
                <div class="metric-value">1.77x</div>
                <div class="metric-subtitle">Odds Ratio (p < 0.001)</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Key Analytical Takeaways
    col_left, col_right = st.columns([1.5, 1])

    with col_left:
        st.subheader("🎯 Core Analytical Framework")
        st.write("""
        1. **Domain-Specific Feature Expansion**: Translates 10 standard questionnaire responses into 3 granular domain sub-scores (*Social Interaction*, *Communication Deficits*, and *Behavioral Atypicality*).
        2. **Identification of the 'Sub-Clinical Bubble'**: Isolates 1,717 patients who sit just below clinical screening thresholds, ensuring sub-clinical cases do not drop out of monitoring.
        3. **Algorithmic Camouflage Detection**: Flags individuals (Age 13+) who exhibit high global trait burdens while scoring 0 on social interaction deficits—isolating social masking.
        4. **Statistical Rigor**: Validated via Chi-Square test of independence ($p = 0.0036$) and Mann-Whitney U test ($p < 0.0001$).
        """)

    with col_right:
        st.subheader("📈 Cohort Breakdown")
        if not df.empty:
            band_counts = df['Diagnostic_Proximity_Band'].value_counts().reset_index()
            band_counts.columns = ['Band', 'Patients']
            fig_pie = px.pie(
                band_counts, 
                names='Band', 
                values='Patients',
                color='Band',
                color_discrete_map={
                    'Clinical Range': '#EF4444',
                    'Borderline / Monitor': '#F59E0B',
                    'Clear Negative': '#10B981'
                },
                hole=0.4
            )
            fig_pie.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color="#F8FAFC")
            )
            st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")
    st.subheader("📋 Dataset Preview (Engineered Features)")
    if not df.empty:
        st.dataframe(df[['Patient_ID', 'Age', 'Sex', 'Age_Group', 'Total_Atypical_Trait_Burden', 'Diagnostic_Proximity_Band', 'Behavioral_Archetype', 'Compensatory_Masking_Flag']].head(10), use_container_width=True)

# -----------------------------------------------------------------------------
# PAGE 2: PATIENT INTAKE & TRAIT CALCULATOR (DETERMINISTIC RULE ENGINE - NO ML)
# -----------------------------------------------------------------------------
elif menu == "🩺 Patient Intake & Trait Calculator":
    st.title("🩺 Interactive Patient Trait Calculator")
    st.caption("Deterministic Clinical Scoring Engine (Rule-Based Summation & Threshold Profiling)")

    st.markdown("""
    > [!NOTE]
    > This tool uses **deterministic clinical scoring rules** derived from the project's 7-tier feature architecture. 
    > It evaluates trait burdens, domain deficits, and adult masking flags **without machine learning**.
    """)

    st.markdown("### 1. Patient Demographics & Background")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        age = st.number_input("Patient Age (Years)", min_value=1, max_value=80, value=24)
    with c2:
        sex = st.selectbox("Sex", ["Male", "Female"])
    with c3:
        jaundice = st.selectbox("Born with Jaundice?", ["No", "Yes"])
    with c4:
        family_asd = st.selectbox("Immediate Family ASD History?", ["No", "Yes"])

    st.markdown("### 2. Behavioral Screening Questionnaire (A1 - A10)")
    st.caption("Select whether the patient exhibits an atypical presentation for each item:")

    col_q1, col_q2 = st.columns(2)

    questions = [
        ("A1: Eye contact when called by name?", "Atypical / Reduced", "Typical / Normal", "Social"),
        ("A2: Ease of making eye contact with others?", "Atypical / Difficult", "Typical / Easy", "Social"),
        ("A3: Pointing to request objects/wants?", "Atypical / Absent", "Typical / Present", "Comm"),
        ("A4: Pointing to share interest with others?", "Atypical / Absent", "Typical / Present", "Comm"),
        ("A5: Engagement in imaginative role-play?", "Atypical / Reduced", "Typical / Active", "Behav"),
        ("A6: Following gaze of others?", "Atypical / Reduced", "Typical / Normal", "Social"),
        ("A7: Attempting to comfort upset individuals?", "Atypical / Absent", "Typical / Active", "Behav"),
        ("A8: Communication style presentation?", "Atypical / Non-standard", "Typical / Standard", "Behav"),
        ("A9: Use of common body gestures (e.g. waving)?", "Atypical / Absent", "Typical / Present", "Comm"),
        ("A10: Unfocused staring into space?", "Atypical / Frequent", "Typical / Rare", "Behav")
    ]

    responses = {}
    for idx, (label, atyp_text, typ_text, domain) in enumerate(questions):
        target_col = col_q1 if idx < 5 else col_q2
        with target_col:
            val = st.radio(label, options=[typ_text, atyp_text], key=f"q_{idx}")
            responses[f"A{idx+1}"] = 1 if val == atyp_text else 0

    st.markdown("---")
    st.markdown("### 3. Deterministic Clinical Trait Calculation")

    if st.button("⚡ Calculate Clinical Trait Profile", type="primary"):
        # 1. Total Burden
        total_burden = sum(responses.values())

        # 2. Domain Sub-Scores
        social_score = responses["A1"] + responses["A2"] + responses["A6"]
        comm_score = (1 - (1 - responses["A3"])) + (1 - (1 - responses["A4"])) + (1 - (1 - responses["A9"]))
        behav_score = (1 - (1 - responses["A5"])) + (1 - (1 - responses["A7"])) + (1 - (1 - responses["A8"])) + responses["A10"]

        # 3. Diagnostic Proximity Band
        if total_burden <= 3:
            proximity_band = "Clear Negative"
            badge_html = '<span class="badge-negative">Clear Negative</span>'
        elif 4 <= total_burden <= 6:
            proximity_band = "Borderline / Monitor"
            badge_html = '<span class="badge-borderline">Borderline / Monitor ⚠️</span>'
        else:
            proximity_band = "Clinical Range"
            badge_html = '<span class="badge-clinical">Clinical Range 🚨</span>'

        # 4. Compensatory Masking Flag
        is_masking = (age >= 13) and (total_burden >= 5) and (social_score == 0)
        masking_status = "High Masking Potential 🎭" if is_masking else "Standard Presentation"

        # Display Results
        res_col1, res_col2, res_col3 = st.columns(3)

        with res_col1:
            st.metric("Total Trait Burden", f"{total_burden} / 10")
            st.markdown(f"**Diagnostic Band:** {badge_html}", unsafe_allow_html=True)

        with res_col2:
            st.metric("Social Interaction Deficit", f"{social_score} / 3")
            st.metric("Communication Deficit", f"{comm_score} / 3")

        with res_col3:
            st.metric("Behavioral Atypicality", f"{behav_score} / 4")
            st.metric("Masking Proxy Flag", masking_status)

        st.markdown("<br>", unsafe_allow_html=True)
        st.info(
            f"**Clinical Recommendation Summary:**\n"
            f"- **Band Evaluation:** Patient falls into the **{proximity_band}** band.\n"
            f"- **Masking Status:** {masking_status}. "
            f"{'Patient exhibits strong global traits but zero social interaction deficit, indicating potential social camouflaging requiring secondary assessment.' if is_masking else 'No social camouflaging flag triggered.'}\n"
            f"- **Familial Factor:** {'Family ASD history adds a 1.77x statistical risk multiplier.' if family_asd == 'Yes' else 'No familial risk factor flagged.'}"
        )

# -----------------------------------------------------------------------------
# PAGE 3: BEHAVIORAL PHENOTYPING & EDA
# -----------------------------------------------------------------------------
elif menu == "🔬 Behavioral Phenotyping & EDA":
    st.title("🔬 Behavioral Phenotyping & Exploratory Data Analysis")
    st.caption("Interactive Exploration of the 6,075 Processed Patient Records")

    if df.empty:
        st.warning("Dataset not available for EDA.")
    else:
        # Filtering Options
        st.markdown("#### Filter Dashboard Data")
        f_col1, f_col2, f_col3 = st.columns(3)
        with f_col1:
            selected_age_group = st.multiselect("Age Group", options=df['Age_Group'].unique(), default=df['Age_Group'].unique())
        with f_col2:
            selected_sex = st.multiselect("Sex", options=df['Sex'].unique(), default=df['Sex'].unique())
        with f_col3:
            selected_band = st.multiselect("Diagnostic Band", options=df['Diagnostic_Proximity_Band'].unique(), default=df['Diagnostic_Proximity_Band'].unique())

        filtered_df = df[
            (df['Age_Group'].isin(selected_age_group)) &
            (df['Sex'].isin(selected_sex)) &
            (df['Diagnostic_Proximity_Band'].isin(selected_band))
        ]

        st.markdown(f"**Filtered Cohort Count:** {len(filtered_df):,} Patients")
        st.markdown("---")

        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.subheader("Behavioral Archetype Distribution")
            archetype_counts = filtered_df['Behavioral_Archetype'].value_counts().reset_index()
            archetype_counts.columns = ['Archetype', 'Count']
            fig_arch = px.bar(
                archetype_counts, 
                x='Count', 
                y='Archetype', 
                orientation='h',
                color='Archetype',
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            fig_arch.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="#F8FAFC"), showlegend=False)
            st.plotly_chart(fig_arch, use_container_width=True)

        with chart_col2:
            st.subheader("Generational Cohort Distribution")
            gen_counts = filtered_df['Generational_Cohort'].value_counts().reset_index()
            gen_counts.columns = ['Generational Cohort', 'Count']
            fig_gen = px.pie(
                gen_counts, 
                names='Generational Cohort', 
                values='Count',
                hole=0.4,
                color_discrete_sequence=px.colors.sequential.Darkmint
            )
            fig_gen.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="#F8FAFC"))
            st.plotly_chart(fig_gen, use_container_width=True)

        st.markdown("---")
        st.subheader("Trait Burden by Gender & Age Group")
        fig_box = px.box(
            filtered_df, 
            x='Age_Group', 
            y='Total_Atypical_Trait_Burden', 
            color='Sex',
            color_discrete_map={'Male': '#38BDF8', 'Female': '#EC4899'}
        )
        fig_box.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="#F8FAFC"))
        st.plotly_chart(fig_box, use_container_width=True)

# -----------------------------------------------------------------------------
# PAGE 4: INFERENTIAL STATISTICAL PROOFS
# -----------------------------------------------------------------------------
elif menu == "⚖️ Inferential Statistical Proofs":
    st.title("⚖️ Inferential Statistics & Hypothesis Testing")
    st.caption("Separating True Clinical Significance from Random Sample Noise")

    st.markdown("""
    Exploratory visualizations show correlation, but inferential statistics provide mathematical proof.
    This module presents the three core statistical tests conducted in the project.
    """)

    t1, t2, t3 = st.tabs(["1. Gender Gap (Chi-Square)", "2. Feature Validity (Mann-Whitney U)", "3. Family Risk (Odds Ratio)"])

    with t1:
        st.subheader("Chi-Square Test of Independence: Gender Presentation Gap")
        st.markdown("""
        * **Null Hypothesis ($H_0$):** Gender and ASD diagnostic screening outcome are independent.
        * **Alternative Hypothesis ($H_1$):** Gender has a statistically significant relationship with diagnostic distribution.
        """)
        
        st.success("✅ Result: **Reject $H_0$** | Chi-Square Statistic: **8.4765** | p-value: **0.0036** ($p < 0.05$)")
        st.write("Demonstrates that gender significantly influences screening presentation rates, supporting the clinical literature on diagnostic gender disparities.")

    with t2:
        st.subheader("Mann-Whitney U Test: Engineered Trait Score Validity")
        st.markdown("""
        * **Null Hypothesis ($H_0$):** The distribution of `Total_Atypical_Trait_Burden` is identical across diagnosed and non-diagnosed cohorts.
        * **Alternative Hypothesis ($H_1$):** The score is significantly higher in diagnosed patients.
        """)

        st.success("✅ Result: **Reject $H_0$** | U-Statistic: **667,116.0** | p-value: **0.0000** ($p < 0.0001$)")
        st.write("Statistically proves that our engineered 7-tier trait burden score successfully separates clinical populations.")

    with t3:
        st.subheader("Odds Ratio Calculation: Familial Risk Multiplier")
        st.markdown("""
        Calculates the exact probability inflation of a positive screening given an immediate family history of ASD.
        """)
        st.info("📊 **Odds Ratio:** **1.77x** | 95% Confidence Interval: **[1.54, 2.03]**")
        st.write("A patient with an immediate family history of ASD is mathematically **1.77 times more likely** to receive a positive screening outcome than a patient without one.")

# -----------------------------------------------------------------------------
# PAGE 5: LIVE CLOUD DEPLOYMENT GUIDE
# -----------------------------------------------------------------------------
elif menu == "🚀 Live Cloud Deployment Guide":
    st.title("🚀 Free Live Deployment Guide (Streamlit Community Cloud)")
    st.markdown("""
    Publish this repository live on the internet for free in under 5 minutes so recruiters, colleagues, or researchers can interact with it online.
    """)

    st.markdown("### Step 1: Push Code to GitHub")
    st.code("""
git add .
git commit -m "Add Streamlit live interactive web app"
git push origin main
    """, language="bash")

    st.markdown("### Step 2: Connect to Streamlit Community Cloud")
    st.markdown("""
    1. Go to [share.streamlit.io](https://share.streamlit.io/).
    2. Log in with your GitHub account.
    3. Click **New App** $\rightarrow$ Select your GitHub repository (`arnav-jain700/Portfolio` or your repo name).
    4. Set Main file path: `app.py`.
    5. Click **Deploy!** 🎈
    """)

    st.success("Your interactive clinical analytics dashboard will be live at `https://<your-app-name>.streamlit.app`!")

# -----------------------------------------------------------------------------
# Footer
# -----------------------------------------------------------------------------
st.markdown("---")
st.caption("Insight Igniters: Beyond the Diagnosis | Portfolio Analytics & Clinical Profiling")
