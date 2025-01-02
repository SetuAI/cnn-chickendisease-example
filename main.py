#from src.cnnClassifier.utils import logger
#logger.info("logger test one")

#from src.cnnClassifier import logger 
#logger.info("logger test second")

from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline


STAGE_NAME = "DATA INGESTION STAGE"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e