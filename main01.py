from sensor.logger import logging
from sensor.exception import SensorException
import sys, os


def tes_logger_and_exception():
    try:
        logging.info("Starting the test_logger_and_exception")
        result = 3/0
        print(result)
        logging.info("Stopping the test_logger_and_exception")
    except Exception as e:
        logging.debug("Stopping the test_logger_and_exception")
        raise SensorException(e, sys)
    
if __name__=="__main__":
    try:
        tes_logger_and_exception()
    except Exception as e:
        print(e)