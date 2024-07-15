import sys
import logger


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_msg="Error occured in Python Script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_msg

class CustomException(Exception):
    
    def __init__(self,error_msg,error_detail:sys):
        super().__init__(error_msg)
        self.error_msg=error_message_detail(error_msg,error_detail)
    
    def __str__(self):
        return self.error_msg


if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logger.logging.info("Divide by Zero Error")
        eror="Divide by Zero"
        raise CustomException(e,sys)
