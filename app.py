import streamlit as st
import joblib
import pandas as pd

# Load the saved models
classifier = joblib.load('classifier_model.pkl')
regressor = joblib.load('regressor_model.pkl')

# Streamlit UI
st.title('Prediksi Penyakit Paru-paru Berdasarkan Fitur')

# Model selection
model_type = st.selectbox('Pilih tipe model:', ['Klasifikasi', 'Regresi'])

# Input fields for features
usia = st.selectbox('Usia', ['Muda', 'Tua'])
jenis_kelamin = st.selectbox('Jenis Kelamin', ['Pria', 'Wanita'])
merokok = st.selectbox('Status Merokok', ['Aktif', 'Pasif'])
bekerja = st.selectbox('Status Bekerja', ['Ya', 'Tidak'])
rumah_tangga = st.selectbox('Status Rumah Tangga', ['Ya', 'Tidak'])
begadang = st.selectbox('Aktivitas Begadang', ['Ya', 'Tidak'])
olahraga = st.selectbox('Aktivitas Olahraga', ['Sering', 'Jarang'])
asuransi = st.selectbox('Asuransi', ['Ada', 'Tidak'])
penyakit_bawaan = st.selectbox('Penyakit Bawaan', ['Ada', 'Tidak'])

# Convert inputs to numeric values using LabelEncoder mappings
input_data = pd.DataFrame([[
    usia, jenis_kelamin, merokok, bekerja, rumah_tangga, begadang, olahraga, asuransi, penyakit_bawaan
]], columns=['Usia', 'Jenis_Kelamin', 'Merokok', 'Bekerja', 'Rumah_Tangga', 'Aktivitas_Begadang', 
             'Aktivitas_Olahraga', 'Asuransi', 'Penyakit_Bawaan'])

# Load label encoders used during training
encoders = joblib.load('label_encoders.pkl')
for column, encoder in encoders.items():
    input_data[column] = encoder.transform(input_data[column])

# Prediction
if st.button('Prediksi'):
    if model_type == 'Klasifikasi':
        prediction = classifier.predict(input_data)
        st.write(f'Prediksi Klasifikasi (Penyakit Paru-paru): {"Ya" if prediction[0] == 1 else "Tidak"}')
    else:
        prediction = regressor.predict(input_data)
        st.write(f'Prediksi Regresi (Estimasi Numerik): {prediction[0]}')
