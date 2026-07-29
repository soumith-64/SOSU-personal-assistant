import os
import time
from config import APP_LOG_FILE


def timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def format_log(message, level):
    time_stamp = timestamp()
    return f"[{time_stamp}] [{level.upper()}] [{message}]"

def write_log(sentence):

    if sentence and sentence.strip():
        os.makedirs(os.path.dirname(APP_LOG_FILE), exist_ok=True)
        
        with open(APP_LOG_FILE, "a", encoding="utf-8") as logging:
            logging.write(f"{sentence}\n")
    else:
        raise ValueError("Log message cannot be empty.")

def info(message):
    write_log(format_log(message, "INFO"))


def warning(message):
    write_log(format_log(message, "WARNING"))


def error(message):
    write_log(format_log(message, "ERROR"))


    
