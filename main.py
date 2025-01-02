

from sensor.exception import SensorException
from sensor.logger import logging
from sensor.utils import get_collection_as_dataframe
import sys, os
from sensor.entity import config_entity
from sensor.components import data_ingestion
from sensor.components import data_validation
from sensor.components import mode_trainer
from sensor.components import data_transformation


if __name__ == '__main__':
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()

        #data ingestion
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = data_ingestion.DataIngestion(data_ingestion_config = data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        #data validation
        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config= training_pipeline_config)
        data_validation = data_validation.DataValidation(data_validation_config=data_validation_config, 
                                        data_ingestion_artifact= data_ingestion_artifact)
        data_validation_artifact = data_validation.initiate_data_validation()

        #data transformation

        data_transformation_config = config_entity.DataTransformationCongig(training_pipeline_config=training_pipeline_config)
        data_transformation = data_transformation.DataTransformation(data_transformation_config=data_transformation_config,
                                                                     data_ingestion_artifact=data_ingestion_artifact)
        data_transformation_artifact = data_transformation.initiate_data_transformation()

        #model trainer
        mode_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
        mode_trainer = mode_trainer.ModelTrainer(model_trainer_config=mode_trainer_config, data_transformation_artifact=data_transformation_artifact)

        model_trainer_artifact = mode_trainer.initiate_model_trainer()

    except Exception as e:
        raise SensorException(e, sys)