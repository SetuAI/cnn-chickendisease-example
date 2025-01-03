from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import Training
from cnnClassifier import logger
import tensorflow as tf

# Ensure TensorFlow's eager execution is enabled
tf.compat.v1.enable_eager_execution()


STAGE_NAME = "TRAINING STAGE"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        
        # add it to endpoint : main.py