#  Crime Case Closure Prediction System

An end-to-end Machine Learning project that predicts whether a reported crime case is likely to be **closed** or remain **open**, based on historical crime data and engineered features.

---

##  Project Overview

This system leverages structured crime data to assist in predictive analysis of case outcomes. By analyzing patterns such as reporting delay, time of occurrence, and categorical attributes (city, crime type, weapon, etc.), the model estimates the likelihood of case closure.

---

##  Tech Stack

- **Language:** Python  
- **Libraries:**  
  - pandas  
  - NumPy  
  - scikit-learn  
  - Streamlit  
- **Model:** Random Forest Classifier  
- **Deployment:** Local Web App (Streamlit)

---

##  Machine Learning Workflow

### 1. Data Preprocessing
- Handled missing values  
- Converted inconsistent datetime formats  
- Cleaned categorical features  

### 2. Feature Engineering
- `report_delay` → Difference between report & occurrence  
- `hour` → Time-based pattern extraction  
- `day_of_week` → Behavioral trends  

### 3. Encoding
- One-hot encoding for categorical variables  
- Ensured consistency between training and inference  

### 4. Model Training
- Algorithm: Random Forest Classifier  
- Applied train-test split  
- Evaluated using:
  - Accuracy  
  - Precision  
  - Recall  
  - F1-score  

### 5. Model Deployment
- Model saved using `pickle`  
- Integrated into Streamlit UI for real-time predictions  

---

##  Application Features

-  Modern UI with gradient design  
-  User-friendly input controls  
-  Real-time prediction  
-  Fast and lightweight  
-  Handles feature alignment dynamically  

---

##  Project Structure
crime-case-prediction/
│
├── app.py # Streamlit application
├── model.pkl # Trained ML model
├── columns.pkl # Feature columns used in training
├── notebook.ipynb # Jupyter Notebook (training pipeline)
├── dataset.csv # Dataset (if included)
└── README.md

---

##  How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/har5hana/Crime-Prediction-System.git
cd crime-case-prediction
pip install streamlit scikit-learn pandas numpy
streamlit run app.py
http://localhost:8501
 Sample Input
Report Delay: 2 days
Hour: 14
Day: Wednesday
City: Pune
Crime Type: Burglary
 Future Improvements
 Add dashboard analytics & visualizations
 Integrate geographic crime mapping
 Hyperparameter tuning for better accuracy
 Deploy on cloud (Streamlit Cloud / AWS / Render)
 Real-time data integration
 Key Learnings
Handling inconsistent real-world datasets
Feature engineering from datetime data
Managing one-hot encoding in production
Deploying ML models as web apps
Debugging environment & dependency issues
```

 License

This project is open-source and available under the MIT License.

 Author

Harshana Yadav

 If you like this project

Give it a ⭐ on GitHub — it helps!

<img width="1894" height="907" alt="Screenshot 2026-04-22 202849" src="https://github.com/user-attachments/assets/b65df97f-4d5e-426c-953e-5d0c2b2d526d" />










