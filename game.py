# from pathlib import Path
# path = Path()
# for file in path.glob('*.py'):
#     print(file)
command = ""
started = False
while True:
    command = input(">").lower()
    if(command == "help"):
        print("""
start -to start the car
stop -to stop the car
quit - to end the race
""")
    elif(command == "start"):
        if started:
            print("car already started")
        else:
            started = True
            print("car starting....")
    elif(command == "stop"):
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car stopped...")
    elif(command == "quit"):
        print("race terminated")
        break
    else:
       print("Sorry unknown command")