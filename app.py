import streamlit as st
import joblib
import numpy as np
import pandas as pd
import sqlite3
import os

# ✅ Ensure 'data' directory exists
os.makedirs("data", exist_ok=True)

# ✅ Connect to SQLite database
conn = sqlite3.connect("data/predictions.db", check_same_thread=False)
cursor = conn.cursor()

# ✅ Create predictions table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gender TEXT,
        ethnicity TEXT,
        education TEXT,
        lunch TEXT,
        prep TEXT,
        prediction TEXT
    )
''')
conn.commit()

# ✅ Load model and encoders
model = joblib.load("model/student_model.pkl")
target_encoder = joblib.load("model/target_encoder.pkl")
label_encoders = joblib.load("model/feature_encoders.pkl")

# ✅ Streamlit UI
st.title("🎓 Student Performance Predictor")

# User input
gender = st.selectbox("Gender", ["female", "male"])
ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
education = st.selectbox("Parental Level of Education", [
    "some high school", "high school", "some college", 
    "associate's degree", "bachelor's degree", "master's degree"
])
lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
prep = st.selectbox("Test Preparation Course", ["none", "completed"])

# Encode inputs
input_data = {
    "gender": label_encoders["gender"].transform([gender])[0],
    "race/ethnicity": label_encoders["race/ethnicity"].transform([ethnicity])[0],
    "parental level of education": label_encoders["parental level of education"].transform([education])[0],
    "lunch": label_encoders["lunch"].transform([lunch])[0],
    "test preparation course": label_encoders["test preparation course"].transform([prep])[0]
}

X_input = np.array([[input_data[col] for col in input_data]])

# Predict and save
if st.button("Predict Performance"):
    prediction = model.predict(X_input)
    predicted_class = target_encoder.inverse_transform(prediction)[0]
    st.success(f"🎯 Predicted Performance Level: **{predicted_class}**")

    # Save to database
    cursor.execute('''
        INSERT INTO student_predictions (gender, ethnicity, education, lunch, prep, prediction)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (gender, ethnicity, education, lunch, prep, predicted_class))
    conn.commit()

# Show saved predictions
st.subheader("📄 Saved Predictions")
if st.checkbox("Show Database Table"):
    df_db = pd.read_sql_query("SELECT * FROM student_predictions", conn)
    st.dataframe(df_db)
