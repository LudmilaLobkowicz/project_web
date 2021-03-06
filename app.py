


import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import requests

CSS = """
h1 {
    color: DarkTurquoise;
}
body {
    background-size: cover;
    background-color: LightCyan;
}
"""

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)



# from project_web.api.fast_web import predict

# st.markdown("""# This is a header
# ## This is a sub header
# This is text""")
image = Image.open('lungs.jpeg')
st.image(image, use_column_width=1)

st.title("🫁 Chest X-Ray Detector 🫁")
#st.write("*Detecting: Bacterial Pneumonia, Viral Pneumonia, COVID-19*")
st.header("*Upload the patient's chest X-Ray below*")

# st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose a jpeg, jpg, png file", type=['png', 'jpg', 'jpeg'])

image = uploaded_file
if image is not None:
    #image = Image.open(uploaded_file)
    # plt.imshow(image) # st.write(data)
    st.image(image, caption='Uploaded X-Ray.', use_column_width=True, width=1)
    st.write("")
    # predict(image)
    # label = predict(image)
    # if label == 0:
    #     st.write("This shit aint working")
    # else:
    #     st.write("our model got results")
#
# url = 'http://taxifare.lewagon.ai/predict_fare/'

col1,col2 = st.beta_columns(2)

#col1,col2 = st.beta_columns(2)
#predict_button = col1.button('Predict on uploaded files')
#test_data = col2.button('Predict on sample data')

st.header("*Normal or Diseased?*")

if st.button('👇 Push to predict 🌌'):
    #url = 'http://127.0.0.1:8000/predict_diseased'
    url = 'https://define-some-container-image-name-p6ejzc3aka-ew.a.run.app/predict_diseased'
    st.write("Predicting...")
    # elem = ('uploaded.jpeg', image, "multipart/form-data")
    # files = {'media': elem}

    elem = {'file': uploaded_file}

    response = requests.post(
        url,
        files=elem
        )

    prediction = response.json()['prediction'][0]
    # st.write(response.json())
    # st.write(prediction)

    if prediction == 'Normal':
        st.success("The results of your Chest X-Ray was normal 🥳")
    elif prediction == 'Diseased':
        st.error("The results of your Chest X-Ray predicts disease ☹️")



st.header("*Classify Disease*")


if st.button('👇 Push to classify 🌌'):
    #url_2 = 'http://127.0.0.1:8000/predict_CXray'
    url_2 = 'https://define-some-container-image-name-p6ejzc3aka-ew.a.run.app/predict_CXray'
    st.write("Classifying...")
    # elem = ('uploaded.jpeg', image, "multipart/form-data")
    # files = {'media': elem}

    elem = {'file': uploaded_file}

    response = requests.post(
        url_2,
        files=elem
        )


    prediction = response.json()['prediction'][0]
    #st.write(response.json())
    #st.write(prediction)

    if prediction == 'Normal':
        st.success("The results of your Chest X-Ray was normal 🥳")
    elif prediction == 'Bacterial Pneumonia':
        st.error("The results of your Chest X-Ray was a Bacterial Pneumonia")
    elif prediction == 'Viral Pneumonia':
        st.error("The results of your Chest X-Ray was a Viral Pneumonia 🦠")
    elif prediction == 'Covid-19':
        st.error("The results of your Chest X-Ray was a Covid-19 infection 🦠")
    elif prediction == 0:
        st.error("Prediction did not work")




