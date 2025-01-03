import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    "class for predicting images"
    def __init__(self,filename):
        self.filename =filename

    
    def predict(self):
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

        if result[0] == 1:
            prediction = 'Healthy'
            return [{ "image" : prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{ "image" : prediction}]