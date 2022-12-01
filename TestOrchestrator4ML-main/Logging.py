import logging

def getLoggerObj():
    logging.basicConfig(filename='Logs.LOG', level=logging.INFO, format='%(asctime)s:::%(name)s:::%(levelname)s:::%(message)s', datefmt='%d-%b-%y %H:%M:%S') 
    loggerObj = logging.getLogger('Log-Logger')
    return loggerObj 
