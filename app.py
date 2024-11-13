import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from google.colab import drive
import requests

# URL raw file CSV di GitHub
url = 'https://github.com/nilatiara/KomputasiPararel/blob/main/predic_tabel.csv'

# Mengunduh dataset dan membaca dengan pandas
df = pd.read_csv(url)

# Tampilkan dataset di Streamlit
st.write("Dataset Penyakit Paru", df)
# Load dataset and sample 50 rows
data = pd.read_csv(file_path).sample(50, random_state=42)

# Encode categorical features
label_encoders = {}
for column in data.columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Split features and target
X = data.drop(columns=['Hasil'])
y = data['Hasil']

# Initialize models
dt_model = DecisionTreeClassifier(random_state=42)
rf_model = RandomForestClassifier(random_state=42)
lr_model = LogisticRegression(random_state=42, max_iter=1000)

# Train models
dt_model.fit(X, y)
rf_model.fit(X, y)
lr_model.fit(X, y)

# Sidebar for user input
st.sidebar.header("Input Features for Prediction")
input_data = {}
for column in X.columns:
    options = label_encoders[column].classes_
    input_data[column] = st.sidebar.selectbox(f"{column}:", options)
    input_data[column] = label_encoders[column].transform([input_data[column]])[0]

# Convert input data to DataFrame
input_df = pd.DataFrame([input_data])

# Model selection
st.sidebar.header("Select Model")
model_option = st.sidebar.selectbox("Choose a model:", ("Decision Tree", "Random Forest", "Logistic Regression"))

# Prediction and Display
if model_option == "Decision Tree":
    prediction = dt_model.predict(input_df)
elif model_option == "Random Forest":
    prediction = rf_model.predict(input_df)
else:
    prediction = lr_model.predict(input_df)

# Decode the prediction result
prediction_text = label_encoders['Hasil'].inverse_transform(prediction)[0]

# Display results
st.title("Prediksi Penyakit Paru")
st.write("Hasil prediksi berdasarkan input data:")
st.write(f"Penyakit Paru: **{prediction_text}**")
