command = ""
started = False
while True:
    command = input("> ")
    if command == "start":
        if started:
          print('car has started....')
        else:
            started = True
            print('car is already started')
    elif command == "stop":

        print('the car has stopped')
    elif command == "help":
        print("""
start- to start the car
stop- to stop the car
quit- to quit
        """)
    elif command == "quit":
        break
    else:
        print("sorry i dont understad that")

