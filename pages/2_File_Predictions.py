import joblib
import pandas as pd
import streamlit as st
import os

# Page config
st.set_page_config(
    page_title = 'Insurance Prediction',
    page_icon = 'img/doctor_icon.png',
)

# Sidebar
st.sidebar.header('File Prediction')

st.sidebar.markdown('''
    This page allows you to make predictions using the model trained in the previous page.
    You can input your own data and see how it affects the insurance price prediction.
''')

st.markdown('Predict medical insurance based using a CSV file.')

# -- Model -- #
model = joblib.load('models/model.pkl')

data = st.file_uploader('Upload your file')
if data:
    df_input = pd.read_csv(data)
    insurance_prediction = model.predict(df_input)
    df_output = df_input.assign(prediction = insurance_prediction)

    st.markdown('Insurance cost prediction:')
    st.write(df_output)
    st.download_button(label = 'Dowload CSV', data = df_output.to_csv(index = False).encode('utf-8'), file_name = 'insurance_prediction.csv', mime = 'text/csv')