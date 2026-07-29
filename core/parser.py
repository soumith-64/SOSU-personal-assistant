from utils import logger


def split_imput(user_input):

    usr_inp_sep = user_input.strip().split(" ")
    command,argument = usr_inp_sep[0],usr_inp_sep[1]
    print(command+"\n"+argument)