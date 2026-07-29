from utils import logger

def check_inp(val):
    usr_inp_sep = val.strip().split(" ")

    if len(usr_inp_sep) == 1:
        command = usr_inp_sep[0]
    elif len(usr_inp_sep) >= 2:
        command,argument = usr_inp_sep[0],usr_inp_sep[1]
    print(command+"\n"+argument)

def split_imput(user_input):
    logger.info(f"User : {user_input}")
    check_inp(user_input)