from config import BASE_DIR,APP_LOG_FILE
import time,os

time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")


def write_log(sentence):

    os.makedirs(APP_LOG_FILE , exist_ok=True)

    with open(APP_LOG_FILE,"a") as logging:
        logging.write(f"{sentence}\n")

def info(message):

    sent = f"[{time_stamp}] Info [{message}] "
    write_log(sent)

def warning(message):
    sent = f"[{time_stamp}] Info [{message}] "
    write_log(sent)

def error(message):
    sent = f"[{time_stamp}] Info [{message}] "
    write_log(sent)
    
