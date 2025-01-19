
command = ""
started = False

while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("Car is already started...")
        else:
            started = True
            print("Car has started...")
    elif command == 'stop':
        if not started:
            print("Car already stopped...")
        else:
            started = False
            print("Car has stopped...")
    elif command == 'help':
        print(""" 
              start - To start the car
              stop - To stop the car
              quit - To exit the game
              """)
    elif command == 'quit':
        print("Thanks for playing!")
        break
    else:
        print("Sorry, I do not understand that! Please type 'help' to see options.")
