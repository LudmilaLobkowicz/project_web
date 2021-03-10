
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import requests
# from project_web.api.fast_web import predict

# st.markdown("""# This is a header
# ## This is a sub header
# This is text""")
st.title("Chest X-Ray Disease Detector")
st.header("Detecting: Bacterial Pneumonia, Viral Pneumonia, COVID-19")
st.header("Upload the patient's chest X-Ray below")

# st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose a jpeg file", type="jpeg")

image = uploaded_file
if image is not None:
    # image = Image.open(uploaded_file)
    # plt.imshow(image) # st.write(data)
    st.image(image, caption='Uploaded X-Ray.', use_column_width=True, width=3)
    st.write("")
    # predict(image)
    # label = predict(image)
    # if label == 0:
    #     st.write("This shit aint working")
    # else:
    #     st.write("our model got results")
#
# url = 'http://taxifare.lewagon.ai/predict_fare/'


st.header("Determine whether your patient has a disease or not.")
st.header("Push the Predict button below:")

if st.button('Predict X_Ray'):
    #url = 'http://127.0.0.1:8000/predict_diseased'
    url = 'http://localhost:8000/predict_diseased'
    st.write("Predicting...")
    # elem = ('uploaded.jpeg', image, "multipart/form-data")
    # files = {'media': elem}

    elem = {'file': uploaded_file}

    response = requests.post(
        url,
        files=elem
        )

    #prediction = response.json()['prediction'][0]
    st.write(response.json())
    #st.write(prediction)

    # if prediction == 'Normal':
    #     st.success("The results of your Chest X-Ray was normal")
    # elif prediction == 'Diseased':
    #     st.warning("The results of your Chest X-Ray should disease")


st.header("Classify which disease your patient has.")
st.header("Push the Classify button below:")

if st.button('Classify Disease'):
    #url_2 = 'http://127.0.0.1:8000/predict_CXray'
    url_2 = 'http://localhost:8000/predict_CXray'
    st.write("Classifying...")
    # elem = ('uploaded.jpeg', image, "multipart/form-data")
    # files = {'media': elem}

    elem = {'file': uploaded_file}

    response = requests.post(
        url_2,
        files=elem
        )


    prediction = response.json()['prediction'][0]
    st.write(response.json())
    st.write(prediction)

    if prediction == 'Normal':
        st.success("The results of your Chest X-Ray was normal")
    elif prediction == 'Bacterial Pneumonia':
        st.warning("The results of your Chest X-Ray was a bacterial_pneumonia")
    elif prediction == 'Viral Pneumonia':
        st.warning("The results of your Chest X-Ray was a viral_pneumonia")
    elif prediction == 'Covid-19':
        st.warning("The results of your Chest X-Ray was a Covid-19 infection")
    elif prediction == 0:
        st.success("prediction did not work")

