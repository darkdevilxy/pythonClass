def commands(inst):
    if inst == "help":
        return f"""
Hello welcome to the help section:

help: to access the help section
run: to run the program
stop: to stop the program
"""
    elif inst == "start":
        return "program initiated"
    elif inst == "stop":
        return "program terminated"
    else:
        return "Unable to execute the code"
    return 0


while 1 > 0:
    command = input("> ")
    command.lower()
    print(commands(command))
