# ❤️ Heart & Stroke Disease Risk Predictor

### Powered by Machine Learning \| Built with Streamlit

🔗 **Live Web App:**\
👉 https://heartstroke.streamlit.app/

This project predicts the risk of **heart disease** using a trained
Machine Learning model.\
Users can input their health parameters and instantly receive a risk
score with visualizations.

------------------------------------------------------------------------

## 🚀 Features

-   🖥️ **Beautiful & Organized UI** built with Streamlit\
-   🤖 **KNN-based ML model**\
-   📊 **Risk Gauge Meter**\
-   🔢 Handles all numeric & categorical inputs\
-   📈 Works with real clinical parameters\
-   ⚡ Fast predictions\
-   📝 Inline explanations & guidance\
-   🛡️ Medical disclaimer included

------------------------------------------------------------------------

## 📷 Screenshots

### 📌 Home / Landing Page

![Screenshot 1](screenshots/Screenshot1.png)

### 📌 Input Form

![Screenshot 2](screenshots/Screenshot2.png)

### 📌 Prediction Result & Gauge

![Screenshot 3](screenshots/Screenshot3.png)

(Your uploaded screenshots should be stored in a folder named
**screenshots/** inside the repo)

------------------------------------------------------------------------

## 🧠 Machine Learning Model Details

-   Algorithm → **K-Nearest Neighbors (KNN)**
-   Preprocessing → **StandardScaler**
-   Model Files:
    -   `knn_heart_model.pkl`
    -   `heart_scaler.pkl`
    -   `heart_columns.pkl`
-   Dataset → UCI Heart Disease Dataset

The model predicts: - **1 → High Risk** - **0 → Low Risk**

------------------------------------------------------------------------

## 🛠️ Tech Stack

  Component         Technology
  ----------------- -----------------
  Frontend          Streamlit
  Backend           Python
  ML Model          Scikit-Learn
  Visualization     Plotly
  Deployment        Streamlit Cloud
  Version Control   Git & GitHub

------------------------------------------------------------------------

## 📦 Installation (Run Locally)

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/Vikaumar/HeartStrokePredictor.git
cd HeartStrokePredictor
```

### 2️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## 📁 Project Structure

    📦 HeartStrokePredictor
     ┣ 📜 app.py
     ┣ 📜 knn_heart_model.pkl
     ┣ 📜 heart_scaler.pkl
     ┣ 📜 heart_columns.pkl
     ┣ 📜 requirements.txt
     ┣ 📂 screenshots
     ┃ ┣ 📜 Screenshot1.png
     ┃ ┣ 📜 Screenshot2.png
     ┃ ┗ 📜 Screenshot3.png
     ┗ 📜 README.md

------------------------------------------------------------------------

## 🌐 Deployment

This app is deployed using **Streamlit Cloud**:\
🌍 https://heartstroke.streamlit.app/

------------------------------------------------------------------------

## ⚕️ Medical Disclaimer

This tool is for **educational purposes only**.\
It does **not** provide medical diagnosis.\
Always consult certified healthcare professionals for medical decisions.

------------------------------------------------------------------------

## 👨‍💻 Developer

**Vikas Kumar**

If you like this project, please ⭐ the repository!

------------------------------------------------------------------------

🎉 *Thank you for exploring this project!*
