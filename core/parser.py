from config import PROMPT
from utils import logger
from core import router


def validate_input(val):

    usr_inp_sep = val.strip().upper().split()

    if len(usr_inp_sep) == 1:
        v_command = usr_inp_sep[0]
        return v_command,""
    else:
        v_command = usr_inp_sep[0]
        v_argument = " ".join(usr_inp_sep[1:])
        return v_command,v_argument
        
def parser_to_route(command,argument):
    
    router.route(command,argument)


def parse_input(user_input):
    logger.info(f"User: {user_input}")
    command,argument = validate_input(user_input)
    parser_to_route(command,argument)
