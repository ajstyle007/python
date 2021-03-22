def getdate():
    import datetime
    print(datetime.datetime.now())
    return datetime.datetime.now()

def clients():
    client = input("enter the client name:\n ")
    if client == "ram":
        choice = input("enter 1 for diet or 2 for exrcise:\n")
        if choice == "1":
            f = open("ram_diet.txt","rt")
            print(f.read())
        elif choice == "2":
            f = open("ram_exr.txt","rt")
            print(f.read())

    elif client == "shyam":
        choice = input("enter 1 for diet or 2 for exrcise:\n")
        if choice == "1":
             f = open("shyam_diet.txt","rt")
             print(f.read())
        elif choice == "2":
            f = open("shyam_exr.txt","rt")
            print(f.read())
    elif client == "calm":
        choice = input("enter 1 for diet or 2 for exrcise:\n")
        if choice == "1":
            f = open("calm_diet.txt", "rt")
            print(f.read())
        elif choice == "2":
            f = open("calm_exr.txt","rt")
            print(f.read())

clients()
getdate()
