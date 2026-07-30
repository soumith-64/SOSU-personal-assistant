from core import startup,assistant 

startup.start()

assistant.run()


from core import parser
from config import PROMPT
from utils import logger

def run():
    while True:

        try :
            input_user = input("User : ")
            if input_user.strip():
                result = parser.parse_input(input_user)
                break

            print(f"{PROMPT} Hi, I'm waiting to hear from you.")
