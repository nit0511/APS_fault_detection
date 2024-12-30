import os, sys
from datetime import datetime
from sensor.logger import logging
from sensor.exception import SensorException

FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
test_size = 0.2


class TrainingPipelineConfig:
    try:

        def __init__(self):
            self.artifact_dir = os.path.join(os.getcwd(), "artifact", f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
    except Exception as e:
        raise SensorException(e,sys)


class DataIngestionConfig:
    try:

        def __init__(self, training_pipeline_config:TrainingPipelineConfig):
            self.database_name = "APS"
            self.collection_name = "Sensor"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_path = os.path.join(self.data_ingestion_dir, "feature",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir, "dataset", TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir, "dataset", TEST_FILE_NAME)
            self.test_size = test_size
    except Exception as e:
        raise SensorException(e, sys)

    def to_dict(self)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e, sys)



class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...
