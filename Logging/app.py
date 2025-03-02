import logging 
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.FileHandler("LOG_FILE"),logging.StreamHandler()]
)


logger=logging.getLogger("ArithmeticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b}={result}")
    return result
def sub(a,b):
    result=a-b
    logger.debug(f"Adding {a}-{b}={result}")
    return result

def divide(a,b):
    try:
        result=a/b
    except ZeroDivisionError:
        logger.error("Division by Zero error ")
        return None


print(add(15,587))
print(sub(2354,456))
print(divide(100,15))