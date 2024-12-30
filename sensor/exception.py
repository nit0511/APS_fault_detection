import sys

def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback details
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename where the error occurred
    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    )
    return error_message


class SensorException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Initialize base Exception with the message
        self.error_message = error_message_details(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message


    
        


        
        
    
    
