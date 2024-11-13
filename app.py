import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model.pkl')

# Streamlit UI to select features and make predictions
st.title('Predict Disease Based on Features')

# Input fields for user to provide features
feature1 = st.number_input('Feature 1')
feature2 = st.number_input('Feature 2')
# Add more features as per your dataset

# When user presses the button, make prediction
if st.button('Predict'):
    input_data = pd.DataFrame([[feature1, feature2]], columns=['Feature 1', 'Feature 2'])
    prediction = model.predict(input_data)
    st.write(f'Prediction: {prediction[0]}')
