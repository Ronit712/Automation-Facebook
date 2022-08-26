import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup", "params")
class Baseclass:
    def get_logger(self):
        """
            Set logger file to get all log information
        """
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('C:\\Users\\CBNITS 219\\PycharmProjects\\PythonAutomationProject3\\Log'
                                          '\\logfiles.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger
