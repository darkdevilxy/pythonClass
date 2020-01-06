# First program written darkdevixy that can take in commands

print("Welcome to the cli program build by Bibek Humagain")
print("Type Help for Help")

loop = 0
carLoopStart = 0
carLoopStop = 0
while loop < 1:
    command = input(f">")
    command = command.lower()
    if command == "help":
        print(f'''Hello here are the list of the commands that you can use:
              1. start: to start the car
              2. stop: to stop the car
              3. help : to access help section''')
    elif command == "start":
        if carLoopStart > 0:
            print(f"Car has already started")
        else:
            print(f"Aye! engine started, "
              f"ready to go")
            carLoopStart += 1
            carLoopStop = 0
    elif command == "stop":
        if carLoopStop > 0:
            print("Car has already stopped")
        else:
            print(f" car stopped ")
            carLoopStop += 1
            carLoopStart = 0
    else:
        print(f"Command is out of the dictionary")


