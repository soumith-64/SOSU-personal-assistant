from config import CLI_SEPARATOR,VERSION,APP_NAME, DESCRIPTION,PROMPT
from utils import logger


def start():   
    print(CLI_SEPARATOR)
    print(f"{APP_NAME} {VERSION}")
    print(f"{DESCRIPTION}")
    print(CLI_SEPARATOR)
    print("Starting SOSU...")
    print("Initialization complete.")
    print(f"{PROMPT} Ready.")
    logger.info("SOSU Started")
print("")
print("")