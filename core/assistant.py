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
            logger.warning("Empty user input received.")
        except KeyboardInterrupt:
            print("Error Keyboard Interrupted")
            logger.error("KeyboardInterrupt")
            break