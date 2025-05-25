
import logging

def test_loggingDemo():

    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("% (asctime)s: %(levelname)s: %(name)s: %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.CRITICAL)
    logger.debug("A debug statement is executed")
    logger.info("information statement")
    logger.warning("something is in warning mode")
    logger.error("A major error has happpened")
    logger.critical("critical issue")