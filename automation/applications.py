
def handle_hello(arg=""):
    print(f"Hello ")
    
def handle_help(arg=""):
    print(f"Executing HELP with argument: {arg}")

def handle_open(arg=""):
    print(f"Executing OPEN with argument: {arg}")

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
