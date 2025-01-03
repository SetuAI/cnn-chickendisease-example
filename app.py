import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load your model (make sure to provide the correct path to your model file)
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('D:\cnn-example\cnn-chickendisease-example\artifacts\prepare_base_model\base_model_updated.h5')
    return model

model = load_model()

def predict(image):
    """ Preprocess the image and predict the class """
    # Resize and normalize the image
    image = image.resize((224, 224))  # Adjust size depending on your model's input
    image = np.array(image)
    image = image / 255.0  # Normalize to [0, 1]
    image = np.expand_dims(image, axis=0)  # Model expects a batch of images

    # Predict
    predictions = model.predict(image)
    return predictions

# Streamlit UI
st.title('Image Classification with CNN')
st.write("Upload an image and the model will predict the class.")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)
    if st.button('Predict'):
        st.write("Predicting...")
        prediction = predict(img)
        st.write(f"Prediction: {prediction}")  # Customize based on how your model outputs predictions