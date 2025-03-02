
### with this file we are checking and learning how it will create logs inside the app.log file which is given as a config in logger.py file from logger import logging 

def addition(a,b):
    logging.debug("the addition operation taking place ")
    return a+b

logging.debug("the addition function is called ")
addition(3445,2342)