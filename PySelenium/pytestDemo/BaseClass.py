import logging

class BaseClass:
    def test_getLogger(self):

        #loggerName = inspect.stack()[1][3]
        logger =logging.getLogger(__name__)
        fileHandler=logging.FileHandler('logfile.log')
        formatter=logging.Formatter("% (asctime)s: %(levelname)s: %(name)s: %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.CRITICAL)
        logger.setLevel(logging.DEBUG)
        return logger