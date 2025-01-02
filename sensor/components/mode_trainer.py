from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from typing import Optional
import os,sys 
from xgboost import XGBClassifier
from sensor import utils
from sklearn.metrics import f1_score


class ModelTrainer:

    def __init__(self, model_trainer_config:config_entity.ModelTrainerConfig,
                 data_transformation_artifact: artifact_entity.DataTranformationArtifact):
        try:
            logging.info(f"{'>>'*20} Model Trainer {"<<"*20}")
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact=data_transformation_artifact
        except Exception as e:
            raise e
        
    def fine_tune(self):
        try:
            # Write code for Grid search cv
            pass
        except Exception as e:
            raise e
    
    def train_model(self,x,y):
        try:
            xgb_clf = XGBClassifier()
            xgb_clf.fit(x,y)
            return xgb_clf
        except Exception as e:
            raise e

    def initiate_model_trainer(self)->artifact_entity.ModelTrainerArtifact:
        try:
            logging.info(f"Loading train and test array")
            train_array = utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_path)
            test_array = utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_path)
            logging.info(f"Splitting input and target feature and both train and test array")
            x_train, y_train = train_array[:,:-1], train_array[:,-1]
            x_test, y_test = test_array[:,:-1], test_array[:,-1]

            logging.info(f"Training model")

            model = self.train_model(x=x_train,y=y_train)
            yhat_train = model.predict(x_train)

            logging.info(f"Calculating train f1_score")
            f1_train_score = f1_score(y_true=y_train, y_pred=yhat_train)

            yhat_test = model.predict(x_test)
            logging.info(f"Calculating test f1_score")
            f1_test_score = f1_score(y_true=y_test, y_pred=yhat_test)

            logging.info(f"train Score: {f1_train_score} and test score: {f1_test_score}")

            # check for overfillting or underfitting or expected score
            logging.info(f"Checking if our model is underfitting or not")
            if f1_test_score < self.model_trainer_config.expected_score:
                raise Exception("Model is not good as it is not able to give expected accuracy: {self.model_trainer_config.expected_score}: Model actual score: {f1_test_score}")
            logging.info(f"Checking if our model is overfitting or not")
            diff = abs(f1_train_score-f1_test_score)
            if diff>self.model_trainer_config.overfitting_threshold:
                raise Exception(f"Train and test score difference {diff} is more than overfitting threshold {self.model_trainer_config.overfitting_threshold}")

            utils.save_object(file_path=self.model_trainer_config.model_path, obj=model)

            # Prepare artifact

            model_trainer_artifact= artifact_entity.ModelTrainerArtifact(model_path=self.model_trainer_config.model_path, f1_train_score=f1_train_score,f1_test_score=f1_test_score)
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
        except Exception as e:
            raise e