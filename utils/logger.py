import os
import time
from config import APP_LOG_FILE


def timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def format_log(message, level):
    time_stamp = timestamp()
    return f"[{time_stamp}] [{level.upper()}] [{message}]"




    
