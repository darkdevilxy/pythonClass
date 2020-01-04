# First program written darkdevixy that can take in commands

print("Welcome to the cli program build by Bibek Humagain")
print("Type Help for Help")

loop = 0
while loop < 1:
    command = input(f">")
    command = command.lower()
    if command == "help":
        print(f'''Hello here are the list of the commands that you can use:
              1. start: to start the car
              2. stop: to stop the car
              3. help : to access help section''')
    elif command == "start":
        print(f"Aye! engine started, "
              f"ready to go")
    elif command == "stop":
        print(f" car stopped ")
        break
    else:
        print(f"Command is out of the dictionary")


