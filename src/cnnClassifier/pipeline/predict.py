import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

"The PredictionPipeline class is designed to take a single image and determine whether it shows signs of Coccidiosis or appears healthy"

class PredictionPipeline:
    "class for predicting images"
    def __init__(self,filename):
        self.filename =filename

    
    def predict(self):
        '''
        First, it loads your trained CNN model from storage. 
        This is like a doctor retrieving all their years of medical knowledge and experience before examining a patient.
        '''
        # load model
        model = load_model(os.path.join("artifacts", "training","model.h5"))

        imagename = self.filename
        # first load the images
        test_image = image.load_img(imagename, target_size = (224,224))
        # then image is converted to array, no passing of raw images
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        # pass image to model
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)
        
        '''
        Explanation of the above code :
        
        prepares the image for analysis through three important steps:

        Loading and resizing the image to 224x224 pixels - the exact size your model expects
        Converting the image to a numerical array that the model can process
        Adding an extra dimension to the array with expand_dims - this is necessary 
        because your model expects to receive batches of images, even when you're only processing one 
        
        result = np.argmax(model.predict(test_image), axis=1)
        where the actual prediction happens. The model.predict() returns probabilities for each class (healthy vs. Coccidiosis), and argmax finds which class had the highest probability.
        '''

        if result[0] == 1:
            prediction = 'Healthy'
            return [{ "image" : prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{ "image" : prediction}]