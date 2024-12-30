from sensor import utils
from sensor.entity import config_entity
from sensor.entity import artifact_entity
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np




class DataIngestion:

    def __init__(self, data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e,sys)
        
    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            logging.info("exploring collection data as panda dataframe")
            # Exploring collection data as panda dataframe
            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name=self.data_ingestion_config.database_name , 
                collection_name=self.data_ingestion_config.collection_name)
            
            logging.info("save data in feature store")
            # Save data in feature store
            df.replace(to_replace="na", value=np.nan, inplace=True)

            logging.info("create featrue store folder")
            #Create feature store folder if not available
            feature_store_path = os.path.dirname(self.data_ingestion_config.feature_store_path)
            os.makedirs(feature_store_path,exist_ok=True)

            logging.info("save df to feature store folder")
            # Save df to feature store folder
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_path, index=False,header=True)

            logging.info("split data set in to train test split")
            # Split dataset into train and test set.
            train_df, test_df = train_test_split(df, test_size=self.data_ingestion_config.test_size,random_state = 42)

            logging.info("Creating dataset directory folder if not available")
            # Create dataset directory
            dataset_dir = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir,exist_ok=True)

            
            logging.info("save train test to feature store folder")
            # save df to feature store folder
            df.to_csv(path_or_buf=self.data_ingestion_config.train_file_path, index=False, header=True)
            df.to_csv(path_or_buf=self.data_ingestion_config.test_file_path, index=False, header=True)

            # Prepare artifact

            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(
                feature_store_file_path=self.data_ingestion_config.feature_store_path,
                train_file_path=self.data_ingestion_config.train_file_path, 
                test_file_path=self.data_ingestion_config.test_file_path)
                
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise SensorException(e,sys)