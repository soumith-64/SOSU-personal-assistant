import os
import time
from config import APP_LOG_FILE, BASE_DIR


def timestamp() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def sent_create(message: str, type_info):
    time_stamp = timestamp()
    return f"[{time_stamp}] [{type_info.upper()}] [{message}]"


def write_log(sentence: str) -> None:
    os.makedirs(os.path.dirname(APP_LOG_FILE), exist_ok=True)

    with open(APP_LOG_FILE, "a", encoding="utf-8") as logging:
        logging.write(f"{sentence}\n")


def check_val(val):

    if val and val.strip():
        write_log(val)
    else:
        raise RuntimeError("Logger error: Log message cannot be empty.")

def info(message):
    sent = sent_create(message, "Info")
    check_val(sent)


def warning(message):
    sent = sent_create(message, "Warning")
    check_val(sent)


def error(message):
    sent = sent_create(message, "Error")
    check_val(sent)
    
