"# student-performance-app" 
# 🎓 Student Performance Predictor

This is a deployed **Machine Learning Web App** built using **Streamlit**, which predicts a student's performance level based on their demographics and learning background. It uses a trained **Random Forest Classifier** and saves results in a local database.

---

## 🚀 Live Demo

🔗 [Click here to try the app](https://student-performance-app-smyrkvpvhfnexuujrwmn8a.streamlit.app/)

---

## 📊 Features

- Input student details like:
  - Gender
  - Race/Ethnicity
  - Parental Education
  - Lunch Type
  - Test Preparation Course
- Predicts performance level: `Low`, `Medium`, or `High`
- Saves predictions to a database
- Shows saved prediction history
- Clean, responsive UI built with Streamlit

---

## 🧠 Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas & NumPy
- SQLite
- Joblib (for model serialization)

---

## 📁 Project Structure

student-performance-app/
├── app.py # Streamlit frontend & logic
├── model/
│ ├── student_model.pkl
│ ├── feature_encoders.pkl
│ └── target_encoder.pkl
├── data/ # Auto-created to store database
├── requirements.txt # Python dependencies
└── README.md # This file

yaml
Copy
Edit

---

## 🔧 Installation (Run Locally)

```bash
git clone https://github.com/Pravis2704/student-performance-app.git
cd student-performance-app
pip install -r requirements.txt
streamlit run app.py

☁️ Deployment
This app is deployed on Streamlit Cloud. To deploy your own version:

Push your code to a public GitHub repo

Go to https://streamlit.io/cloud

Click "New App"

Select your repo and app.py as the entry point

Click Deploy

📚 Dataset Info
Based on the Students Performance in Exams Dataset from Kaggle.

👨‍💻 Author
Prathmesh Ravindra Salunke
AIML Engineering Student @ RIT Islampur

📄 License
This project is for educational purposes. Free to use with attribution.

yaml
Copy
Edit

---

## ✅ After This

1. Paste this into your `README.md`
2. Push to GitHub:
```bash
git add README.md
git commit -m "Add professional README"
git push
Now your GitHub repo will look clean and professional 💼

