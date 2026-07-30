from core import startup,parser

startup.start()
input_user = input()
result = parser.parse_input(input_user)

if result:
    command, argument = result
