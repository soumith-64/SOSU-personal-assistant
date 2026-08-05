import sys
import subprocess

open_app = lambda app,mac_app : subprocess.Popen(["open","-a",mac_app] if sys.platform == "darwin" else [app])

applications_ava = {
    "notepad": ("notepad", "TextEdit"),
    "paint": ("mspaint", "Preview"),
    "cmd": ("cmd", "Terminal"),
    "explorer": ("explorer", "Finder"),
    "calculator": ("calc", "Calculator"),
}

def handle_hello(arg=""):
    print(f"Hello, Hi there ")
    
def handle_help(arg=""):
    print(f"Executing HELP with argument: {arg}")

def handle_open(arg=""):

    arg = arg.strip().lower()
    print(f"Executing OPEN with argument: {arg}")
    app_info  = applications_ava.get(arg)
    if app_info:
        win_app,mac_app = app_info
        open_app(win_app,mac_app)
    else:
        print("No app found")

def handle_close(arg=""):
    print(f"Executing CLOSE with argument: {arg}")

def handle_search(arg=""):
    print(f"Executing SEARCH with argument: {arg}")

def handle_calculate(arg=""):
    print(f"Executing CALCULATE with argument: {arg}")

def handle_weather(arg=""):
    print(f"Executing WEATHER with argument: {arg}")

def handle_exit(arg=""):
    print("Exiting application...")

def handle_about(arg=""):
    print("Executing ABOUT: SOSU Voice Assistant v1.0")

def handle_default(arg=""):
    print("Executing Default: SOSU Voice Assistant v1.0")
