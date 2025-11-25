
# 🚦 Road Accidents Analytics & Prediction Dashboard  

A complete data-driven dashboard built with **Streamlit**, providing insights into Nigerian road accidents through **exploratory analysis, geospatial mapping**, and **machine‑learning predictions**.  

This repository contains the full workflow — from **data engineering**, **feature enrichment**, **visual analytics**, to **predictive modelling** — wrapped inside an interactive, user‑friendly web application.

---

## 📌 Key Features  

### 🔍 **1. Exploratory Analysis (Analysis Tab)**  
Understand accident patterns across states, seasons, months, and weather conditions.  
- Choose a **category** (e.g., STATE, MONTH, SEASON)  
- Select an **aggregation method** (Sum, Average, Count)  
- Visualize using **Bar, Line, Pie, Area, Scatter, Histogram**, all powered by Plotly  
- Fully dynamic and interactive  

---

### 🗺️ **2. Geospatial Accident Mapping (Map Analysis Tab)**  
Visualize accident severity on a real map using **latitude & longitude**.  
- View distributions of **Fatal**, **Serious**, **Minor**, or **Total Cases**  
- Bubble size and color intensity reflect accident magnitude  
- Uses **Mapbox + Plotly** for interactive zooming and exploration  

---

### 🤖 **3. Machine Learning Predictions (Predictions Tab)**  
Predict accident severity levels using trained **classification models**.  
- Supports SVC, Logistic Regression, RandomForest, XGBoost (depending on your model folder)  
- Model metrics (Accuracy, Precision, Recall, F1, Confusion Matrix) are shown  
- Accepts user input for forecasting accident severity  

---

## 🧱 Project Structure  

```
road-accidents-analytics/
│
├── data/
│   ├── weather_accidents.csv
│   ├── state_coordinates.csv
│   └── cleaned_accidents_data.csv
│
├── pages/
│   ├── main.py
│   ├── analysis_page.py
│   ├── map_analysis_page.py
│   └── predictions_page.py
│
├── utils/
│   └── combine_data.py
│
├── models/
│   └── trained_model.pkl
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the App  

### **1. Clone the Repository**
```
git clone https://github.com/thatquams/road-accidents-analytics.git
cd road-accidents-analytics
```

### **2. Create a Virtual Environment**
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scriptsctivate     # Windows
```

### **3. Install Dependencies**
```
pip install -r requirements.txt
```

### **4. Launch Streamlit**
```
streamlit run pages/main.py
```

---

## 🧭 Navigation Guide  

| Section | What You Can Do |
|--------|------------------|
| **Analysis** | Explore accident patterns using interactive charts and aggregations. |
| **Map Analysis** | View accidents on a geospatial map using severity filters. |
| **Predictions** | Input features to estimate accident severity using ML. |

---

## 🧪 Data Processing  

Data was enriched using:  
- **Weather parameters**  
- **State geolocation coordinates**  
- **Season & month metadata**  
- **Severity columns (Fatal, Serious, Minor)**  

The cleaned dataset is automatically generated using  
`utils/combine_data.py`.

---

## 🤖 Machine Learning Overview  

Models were evaluated using:  
- Accuracy  
- Precision  
- Recall  
- F1 score  
- Confusion Matrix  
- Cross‑validation  

Best-performing model: **Support Vector Classifier (SVC)**  

---

## 🛠️ Technologies  

- **Python**  
- **Streamlit**  
- **Pandas, NumPy**  
- **Plotly Express**  
- **Scikit‑learn**  
- **Mapbox / Scatter Mapbox**  

---

## 🌟 Badges  

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)  
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)  
![Plotly](https://img.shields.io/badge/Plotly-Interactive-0099ff?logo=plotly)  
![License](https://img.shields.io/badge/License-MIT-green)  
![Status](https://img.shields.io/badge/Status-Active-success)  

---


---

---

## 👤 Author  
**Abdulraheem Quwam**  
Data Analyst | Machine Learning | Data Engineering  
GitHub: [thatquams](https://github.com/thatquams)

