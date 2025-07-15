import pickle
import pandas as pd
import streamlit as st
import joblib
import os

# Page config
st.set_page_config(
    page_title = 'Insurance Prediction',
    page_icon = 'img/doctor_icon.png',
)

# Sidebar
st.sidebar.header('What If Prediction')
st.sidebar.markdown('''
    This page allows you to make predictions using the model trained in the previous page.
    You can input your own data and see how it affects the insurance price prediction.
''')

# Page title
st.title('Insurance Prediction')

# -- Parametros -- #
age = st.number_input(label = 'Age', value = 18, min_value = 18, max_value = 120, step = 1)
bmi = st.number_input(label = 'BMI', value = 30.0)
children = st.slider(label = 'Children', min_value = 0, max_value = 5)
smoker = st.selectbox(label = 'Smoker', options = ['yes', 'no'])

# -- Model -- #
model = joblib.load('models/model.pkl')

def prediction():
    df_input = pd.DataFrame([{
        'age': age,
        'bmi': bmi,
        'children': children,
        'smoker': smoker
    }])
    prediction = model.predict(df_input)[0]
    return prediction

# Predict
if st.button('Predict'):
    try:
        insurance_cost = prediction()
        st.success(f'**Predicted insurance price:** ${insurance_cost:,.2f}')
    except Exception as error:
        st.error(f"Couldn't predict the input data. The following error occurred: \n\n{error}")
