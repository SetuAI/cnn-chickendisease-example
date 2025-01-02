# cnn-chickendisease-example
repo contains a CNN pipeline example

dataset : https://www.kaggle.com/datasets/allandclive/chicken-disease-1


Workflows
Update config.yaml
Update params.yaml
Update the entity
Update the configuration manager in src config
Update the components
Update the pipeline
Update the main.py
Update the app.py

In terms of model selection for image classification , we are using VGG16
https://keras.io/api/applications/vgg/#vgg16-function

In artifacts, we download the base model base_model.h5
Model has 2 layers : convo and dense 
we will making changes to the dense layer to make it suitable for our dataset
and merging the model and saving that as updated version 
we save the model in .h5 format

h5 format is a binary format that can be used to save and load models in Keras


Parameters :
AUGMENTATION: True
IMAGE_SIZE: [224, 224, 3] # as per VGG 16 model (input shape)
BATCH_SIZE: 16
INCLUDE_TOP: False
EPOCHS: 1
CLASSES: 2
WEIGHTS: imagenet
LEARNING_RATE: 0.01

AUGMENTATION : True, we are using data augmentation to increase the size of the dataset
IMAGE_SIZE : [224, 224, 3] as per VGG 16 model
BATCH_SIZE : 16, we are using batch size of 16
INCLUDE_TOP : False, we are not including the top layer of the VGG 16 model
EPOCHS : 1, we are using 1 epoch for training
CLASSES : 2, we are using 2 classes for classification
WEIGHTS : imagenet, we are using imagenet weights for the model, we want pretrained version
