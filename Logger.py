from Models import Logger
import logging

def setLog(event,date,message):
    log = Logger(event,date,message)
    return log

def logInfo(log):
    logging.info(f"{log.event} | {log.date} | C#INFO | {log.message}")

def logWarning(log):
    logging.warning(f"{log.event} | {log.date} | C#WARNING | {log.message}")

def logError(log):
    logging.error(f"{log.event} | {log.date} | C#ERROR | {log.message}")

def logException(log,exception):
    logging.exception(f"{log.event} | {log.date} | C#EXCEPTION | {log.message} | {exception}")

def example():
    logError(setLog("Test event","2021-01-01","This is an example message"))