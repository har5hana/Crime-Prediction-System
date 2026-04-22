import streamlit as st
import pickle
import pandas as pd

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="Crime Prediction System",
    page_icon="🚔",
    layout="wide"
)

# -------------------- LOAD --------------------
model = pickle.load(open('model.pkl','rb'))
columns = pickle.load(open('columns.pkl','rb'))

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #00ffe5;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #cfd8dc;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(0,255,229,0.2);
}

.result-box {
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}

.success {
    background-color: rgba(0,255,0,0.2);
    color: #00ffae;
}

.error {
    background-color: rgba(255,0,0,0.2);
    color: #ff4b4b;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown('<div class="title">🚔 Crime Case Closure Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered prediction system using Machine Learning</div>', unsafe_allow_html=True)

# -------------------- LAYOUT --------------------
col1, col2 = st.columns([1,1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    st.subheader("📊 Input Details")

    report_delay = st.number_input("Report Delay (days)", min_value=0)
    hour = st.slider("Hour of Crime", 0, 23)
    day_of_week = st.selectbox(
        "Day of Week",
        ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    )

    day_map = {
        "Monday":0,"Tuesday":1,"Wednesday":2,
        "Thursday":3,"Friday":4,"Saturday":5,"Sunday":6
    }

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    st.subheader("🤖 Prediction Result")

    if st.button("🔍 Predict", use_container_width=True):

        input_data = pd.DataFrame([[
            report_delay,
            hour,
            day_map[day_of_week]
        ]], columns=['report_delay','hour','day_of_week'])

        for col in columns:
            if col not in input_data.columns:
                input_data[col] = 0

        input_data = input_data[columns]

        result = model.predict(input_data)[0]

        if result == 1:
            st.markdown(
                '<div class="result-box success">✅ Case Likely CLOSED</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="result-box error">❌ Case Likely NOT CLOSED</div>',
                unsafe_allow_html=True
            )

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- FOOTER --------------------
#st.markdown("""
#<hr style="border:1px solid #444;">
#<center>Built with ❤️ using Streamlit | ML Project</center>
#""", unsafe_allow_html=True)