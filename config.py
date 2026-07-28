import os,time

APP_NAME = "SOSU"
VERSION = "0.0.1"
AUTHOR = "Soumith.J.V"
DEBUG_MODE = True
PROMPT =  "SOSU >"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


LOG_DIR = os.path.join(BASE_DIR, "logs")
APP_LOG_FILE = os.path.join(LOG_DIR, "app.log")
COMMAND_LOG_FILE = os.path.join(LOG_DIR, "commands.log")
ERRORS_LOG_FILE = os.path.join(LOG_DIR, "errors.log")

CLI_SEPARATOR = "=" * 40
WELCOME_MESSAGE = "Type 'help' to see available commands."