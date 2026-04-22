🚔 Crime Case Closure Prediction System

An end-to-end Machine Learning project that predicts whether a reported crime case is likely to be closed or remain open, based on historical crime data and engineered features.

The project includes:

Data preprocessing & feature engineering
Model training using Random Forest
Model serialization with pickle
Deployment using Streamlit
📌 Project Overview

This system leverages structured crime data to assist in predictive analysis of case outcomes. By analyzing patterns such as reporting delay, time of occurrence, and categorical attributes (city, crime type, weapon, etc.), the model estimates the likelihood of case closure.

⚙️ Tech Stack
Language: Python
Libraries:
pandas
NumPy
scikit-learn
Streamlit
Model: Random Forest Classifier
Deployment: Local Web App (Streamlit)
🧠 Machine Learning Workflow
1. Data Preprocessing
Handled missing values
Converted inconsistent datetime formats
Cleaned categorical features
2. Feature Engineering
report_delay → difference between report & occurrence
hour → time-based pattern extraction
day_of_week → behavioral trends
3. Encoding
One-hot encoding for categorical variables
Ensured consistency between training and inference
4. Model Training
Algorithm: Random Forest Classifier
Train-test split applied
Evaluated using accuracy, precision, recall, F1-score
5. Model Deployment
Model saved using pickle
Integrated into Streamlit UI for real-time predictions
🌐 Application Features
🎨 Modern UI with gradient design
📊 User-friendly input controls
🤖 Real-time prediction
⚡ Fast and lightweight
🧩 Handles feature alignment dynamically
📂 Project Structure
crime-case-prediction/
│
├── app.py                # Streamlit application
├── model.pkl            # Trained ML model
├── columns.pkl          # Feature columns used in training
├── notebook.ipynb       # Jupyter Notebook (training pipeline)
├── dataset.csv          # Dataset (if included)
└── README.md
🚀 How to Run Locally
1. Clone the repository
git clone https://github.com/har5hana/Crime-Prediction-System.git
cd crime-case-prediction
2. Install dependencies

pip install streamlit scikit-learn pandas numpy
3. Run the application
streamlit run app.py
4. Open in browser
http://localhost:8501
📊 Sample Input
Report Delay: 2 days
Hour: 14
Day: Wednesday
City: Pune
Crime Type: Burglary
📈 Future Improvements
📊 Add dashboard analytics & visualizations
🌍 Integrate geographic crime mapping
⚙️ Hyperparameter tuning for better accuracy
☁️ Deploy on cloud (Streamlit Cloud / AWS / Render)
🔄 Real-time data integration
🧠 Key Learnings
Handling inconsistent real-world datasets
Feature engineering from datetime data
Managing one-hot encoding in production
Deploying ML models as web apps
Debugging environment & dependency issues

📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Harshana Yadav

⭐ If you like this project

Give it a star ⭐ on GitHub - it helps!
