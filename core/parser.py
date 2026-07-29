from config import PROMPT
from utils import logger


def check_inp(val):
    
    if not val or not val.strip():
        logger.warning("Empty user input received.")
        print(f"{PROMPT} Hi, I'm waiting to hear from you.")
        return

    usr_inp_sep = val.strip().split()

    if len(usr_inp_sep) == 1:
        command = usr_inp_sep[0]
        print(f"Command: {command}")
    else:
        command = usr_inp_sep[0]
        argument = " ".join(usr_inp_sep[1:])
        print(f"Command: {command}\nArgument: {argument}")


def split_input(user_input):
    logger.info(f"User: {user_input}")
    check_inp(user_input)