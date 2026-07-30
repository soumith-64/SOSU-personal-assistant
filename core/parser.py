from config import PROMPT
from utils import logger


def validate_input(val):

    if not val or not val.strip():
        logger.warning("Empty user input received.")
        print(f"{PROMPT} Hi, I'm waiting to hear from you.")
        return "", ""

    usr_inp_sep = val.strip().split()

    if len(usr_inp_sep) == 1:
        command = usr_inp_sep[0]
        return command,""
    else:
        command = usr_inp_sep[0]
        argument = " ".join(usr_inp_sep[1:])
        return command,argument
        


def parse_input(user_input):
    logger.info(f"User: {user_input}")
    command,argument = validate_input(user_input)

    if not command and not argument:
        return

    return command, argument