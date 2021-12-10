import streamlit as st
import tensorflow as tf
import streamlit as st

@st.cache(allow_output_mutation=True)

def load_model():
    model=tf.keras.models.load_model("C:\\Users\\ontor\\Downloads\\mymodel.hdf5")
    return model
with st.spinner('Model is being loaded..'):
    model=load_model()
    
st.write("""
         # Malaria-infected Cell Classification
         """
         )

file = st.file_uploader("Please upload a cell image file", type=["jpg", "png"])
import cv2
from PIL import Image, ImageOps
import numpy as np

def import_and_predict(image_data, model):
    size = (68,68)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis,...]
    prediction = model.predict(img_reshape)
    
    return prediction

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    if predictions == [[1.]]:
        string = "The patient doesn't have malaria infected cells"
    else:
        string = "The patient has malaria infected cells"
    st.success(string)
        
    



        
