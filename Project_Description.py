import streamlit as st

st.set_page_config(
    page_title = 'Insurance Prediction',
    page_icon = 'img/doctor_icon.png',
)

st.sidebar.header('Project Description')

st.write('# Welcome to the Insurance Prediction App! 🩺')
st.write('\n\n')

st.image('img/hospital.jpg')
st.write('\n\n')

st.markdown(
    """
    Medical insurance prediction is crucial in healthcare as is predicts medical costs and help stakholders allocate resoucers efficiently.
    By leveraging historical data, machine learning models can identify cost drivers, forecast expenses, and optimize insurance pricing.

    This app aims to predict the insurance cost using input features like:
    - Age
    - BMI
    - Number of children
    - Smoker status
    """
)

st.success('Please **go to the next page** to get the predictions.')

