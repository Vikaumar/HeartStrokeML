import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go


# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------
st.set_page_config(
    page_title="Heart Disease Risk Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# -------------------------------------------------------
# CUSTOM CSS - Professional & Minimal
# -------------------------------------------------------
st.markdown("""
<style>
    * { margin: 0; padding: 0; }
    
    .main { padding: 1.5rem 3rem !important; }
    
    [data-testid="stAppViewContainer"] { padding-top: 0.5rem !important; }
    
    [data-testid="stVerticalBlock"] > :first-child { margin-top: 0 !important; }
    .stTabs [data-baseweb="tab-list"] { gap: 1rem; }
    
    .header-section { margin-bottom: 1.5rem; }
    .header-title { 
        color: #1a1a1a; 
        font-size: 2rem; 
        font-weight: 600; 
        margin-bottom: 0.5rem;
    }
    
    .header-subtitle {
        color: #666;
        font-size: 0.95rem;
        font-weight: 400;
        margin-bottom: 0;
    }
    
    .section-label {
        color: #1a1a1a;
        font-size: 0.85rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 1rem;
        margin-top: 0.5rem;
    }
    
    .input-wrapper {
        background: #fafafa;
        padding: 1.25rem;
        border-radius: 6px;
        border: 1px solid #e5e5e5;
        margin-bottom: 0.75rem;
    }
    
    .prediction-result {
        padding: 2rem;
        border-radius: 8px;
        text-align: center;
        font-weight: 600;
        margin: 1.5rem 0;
    }
    
    .high-risk {
        background: #fef2f2;
        border: 1px solid #fca5a5;
        color: #dc2626;
    }
    
    .low-risk {
        background: #f0fdf4;
        border: 1px solid #86efac;
        color: #15803d;
    }
    
    .risk-score-text {
        font-size: 0.9rem;
        opacity: 0.85;
        margin-top: 0.5rem;
    }
    
    .info-section {
        background: #f9fafb;
        padding: 1rem 1.25rem;
        border-radius: 6px;
        border-left: 3px solid #9ca3af;
        margin: 1rem 0;
        font-size: 0.9rem;
        color: #4b5563;
        line-height: 1.6;
    }
    
    .button-primary {
        width: 100%;
    }
    
    .footer-text {
        text-align: center;
        color: #999;
        font-size: 0.85rem;
        margin-top: 3rem;
    }
    
    [data-testid="stMetricValue"] { font-size: 1.8rem !important; }
    
    .stExpander { border: 1px solid #e5e5e5 !important; }
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------------
# LOAD MODELS
# -------------------------------------------------------
@st.cache_resource
def load_models():
    try:
        model = joblib.load("knn_heart_model.pkl")
        scaler = joblib.load("heart_scaler.pkl")
        columns = joblib.load("heart_columns.pkl")
        return model, scaler, columns
    except:
        st.error("Missing model files. Place all .pkl files in the same folder.")
        st.stop()


model, scaler, expected_columns = load_models()


# -------------------------------------------------------
# HEADER
# -------------------------------------------------------
st.markdown('<div class="header-section"><div class="header-title">Heart Disease Risk Predictor</div><div class="header-subtitle">Assess your cardiovascular health with machine learning analysis</div></div>', unsafe_allow_html=True)


# -------------------------------------------------------
# MAIN LAYOUT
# -------------------------------------------------------
col1, col2 = st.columns([3, 1], gap="large")

# ===============================
# LEFT COLUMN - INPUT FORM
# ===============================
with col1:
    
    tab1, tab2, tab3 = st.tabs(["Personal Information", "Clinical Measurements", "Cardiac Metrics"])
    
    # -------- TAB 1: BASIC INFO --------
    with tab1:
        st.markdown('<div class="section-label">Personal Details</div>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2, gap="medium")
        
        with c1:
            age = st.slider("Age", 18, 100, 40, help="Your age in years")
            sex = st.selectbox("Sex", ["M", "F"], help="Biological sex")
        
        with c2:
            chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"], help="Type of chest pain experienced")
            exercise_angina = st.selectbox("Exercise Angina", ["Y", "N"], help="Chest pain induced by exercise")
    
    
    # -------- TAB 2: CLINICAL TESTS --------
    with tab2:
        st.markdown('<div class="section-label">Clinical Measurements</div>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2, gap="medium")
        
        with c1:
            resting_bp = st.number_input("Resting Blood Pressure (mmHg)", 80, 200, 120, help="BP when at rest")
            cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200, help="Total cholesterol level")
        
        with c2:
            fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1], format_func=lambda x: "Yes" if x else "No", help="Fasting glucose level")
            resting_ecg = st.selectbox("Resting ECG Result", ["Normal", "ST", "LVH"], help="ECG reading at rest")
    
    
    # -------- TAB 3: ADVANCED METRICS --------
    with tab3:
        st.markdown('<div class="section-label">Advanced Cardiac Metrics</div>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2, gap="medium")
        
        with c1:
            max_hr = st.slider("Maximum Heart Rate (bpm)", 60, 220, 150, help="Highest heart rate achieved")
        
        with c2:
            oldpeak = st.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0, 0.1, help="ST segment depression")
            st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"], help="Slope of ST segment")


# ===============================
# RIGHT COLUMN - PREDICTION
# ===============================
with col2:
    st.markdown('<div class="section-label">Assessment</div>', unsafe_allow_html=True)
    
    predict = st.button("Analyze", type="primary", use_container_width=True, key="predict_btn")
    
    if predict:
        # Build feature dictionary
        raw = {
            "Age": age,
            "RestingBP": resting_bp,
            "Cholesterol": cholesterol,
            "FastingBS": fasting_bs,
            "MaxHR": max_hr,
            "Oldpeak": oldpeak,
            f"Sex_{sex}": 1,
            f"ChestPainType_{chest_pain}": 1,
            f"RestingECG_{resting_ecg}": 1,
            f"ExerciseAngina_{exercise_angina}": 1,
            f"ST_Slope_{st_slope}": 1,
        }
        
        df = pd.DataFrame([raw])
        
        for col in expected_columns:
            if col not in df:
                df[col] = 0
        
        df = df[expected_columns]
        scaled = scaler.transform(df)
        
        prediction = model.predict(scaled)[0]
        prob = model.predict_proba(scaled)[0][1] * 100
        
        # Display result
        risk_class = "high-risk" if prediction == 1 else "low-risk"
        risk_label = "High Risk" if prediction == 1 else "Low Risk"
        
        st.markdown(f'<div class="prediction-result {risk_class}"><div style="font-size: 1.3rem;">{risk_label}</div><div class="risk-score-text">{prob:.1f}% risk score</div></div>', unsafe_allow_html=True)
        
        # Gauge chart
        gauge_color = "#dc2626" if prediction == 1 else "#15803d"
        
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prob,
            number={"suffix": "%", "font": {"size": 24}},
            gauge={
                "axis": {"range": [0, 100], "tickfont": {"size": 11}},
                "bar": {"color": gauge_color, "thickness": 0.15},
                "steps": [
                    {"range": [0, 30], "color": "#f0fdf4"},
                    {"range": [30, 70], "color": "#fef3f2"},
                    {"range": [70, 100], "color": "#fef2f2"}
                ],
                "threshold": {
                    "line": {"color": "#999", "width": 2},
                    "thickness": 0.75,
                    "value": prob
                }
            }
        ))
        
        fig.update_layout(
            height=280,
            margin=dict(l=20, r=20, t=20, b=20),
            font=dict(size=12, family="Arial, sans-serif"),
            plot_bgcolor="white",
            paper_bgcolor="white"
        )
        
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


# -------------------------------------------------------
# INFO SECTION
# -------------------------------------------------------
st.markdown("---")

st.markdown('<div class="section-label" style="margin-top: 2rem;">Additional Information</div>', unsafe_allow_html=True)

with st.expander("About Risk Factors", expanded=False):
    st.markdown("""
    **Key factors affecting heart disease risk:**
    
    - **Age & Sex** — Risk increases with age; males typically have higher risk at younger ages
    - **Chest Pain Type** — Different patterns indicate different severity levels
    - **Blood Pressure & Cholesterol** — Higher levels increase artery blockage risk
    - **Heart Rate & Exercise Response** — How your heart responds to stress matters
    - **ECG Findings** — Shows electrical activity of the heart
    """)

with st.expander("Disclaimer", expanded=False):
    st.markdown("""
    This tool is for **educational and informational purposes only**. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for personalized medical guidance.
    """)

st.markdown('<div class="footer-text">Heart Disease Risk Predictor | Developed by Vikas</div>', unsafe_allow_html=True)