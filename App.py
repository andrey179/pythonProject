game = ""
started = False
while True:
    game = input('> ').lower()
    if game == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif game == "start":
        if started:
            print("car is already started!")
        else:
            started = True
            print('car has started')
    elif game == "stop":
        if not started:
            print('Car is already stopped')
        else:
            started = False
            print('the car has stopped')
    elif game == "quit":
        break
    else:
        print("I don't understand that, for more type help")






