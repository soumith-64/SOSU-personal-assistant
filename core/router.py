from automation import applications
from utils import logger

route_command = {
    "HELLO": applications.handle_hello,
    "HELP": applications.handle_help,
    "OPEN": applications.handle_open,
    "CLOSE": applications.handle_close,
    "SEARCH": applications.handle_search,
    "CALCULATE": applications.handle_calculate,
    "WEATHER": applications.handle_weather,
    "EXIT": applications.handle_exit,
    "ABOUT": applications.handle_about,
}


def route(command,argument):
        
        handler = route_command.get(command,applications.handle_default)
        if handler:
                
            handler(argument)
            logger.info(f"Routing command {command} argument {argument}")

