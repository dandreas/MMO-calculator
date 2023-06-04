import db

cont = True

while cont:
    userInput = input(">")
    inputList = userInput.split()

    match inputList[0]:
        case "help":
            print("Test")
        case "init":
            print("Initializing database...")
            db.initDb()
            print("Database initialized!")
        case "add":
            print("Add")
        case "calc":
            print("cqlc")
        case "exit":
            print("Exiting...")
            cont = False