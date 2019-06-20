isStarted = False

while True:
    command = input("> ").lower()

    if command == 'help':
        msg = '''
start - to start the car
stop - to stop the car
quit - to exit
        '''
        print(msg)

    elif command == 'start':
        if(isStarted):
            print("Car is already started...")
        else:
            print("Car started...Ready to go!")
            isStarted = True

    elif command == 'stop':
        if (not isStarted):
            print("Car is already stopped...")
        else:
            print("Car stopped")
            isStarted = False

    elif command == 'quit':
        break

    else:
        print("I don't understand that...")
