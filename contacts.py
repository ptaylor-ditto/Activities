def contacts():
    import os, csv, webbrowser, time, random
    from attemptings import attemptings
    from csv import reader
    from main import main
    def cls():
        os.system('cls')
    action = ""
    videos = ['https://www.youtube.com/watch?v=CVCuN_q1K_g', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://www.youtube.com/watch?v=OQj4bQEu-xA', 'https://www.youtube.com/watch?v=vm112M4ToLM', 'https://www.youtube.com/watch?v=cvh0nX08nRw', 'https://www.youtube.com/watch?v=jDwVkXVHIqg', 'https://www.youtube.com/watch?v=wrdK57qgNqA', 'https://www.youtube.com/watch?v=gM4S9lPyUUA', 'https://www.youtube.com/watch?v=8zEQeHcKMXM', 'https://www.youtube.com/watch?v=NW-qSGZByH8']
    #Login or Create
    new = ""
    while new.lower() != "leave" and action.lower() != "stop" and action.lower() != "leave":
        cls()
        new = input("What would you like to do?\n   Login   Create   Delete\n")
        while new.lower() != "create" and new.lower() != "login" and new.lower() != "delete" and new.lower() != "leave":
            cls()
            new = input("What would you like to do?\n   Login   Create   Delete\n")
        #if you want to create
        cont = 1
        if new.lower() == "create":
            cls()
            account = input("What is the name of the account?\n")
            cls()
            passwords = input("What is the password of the account?\n")
            if os.path.exists(f"{account}_____.csv"):
                cls()
                print("This account already exists.")
                time.sleep(2)
                cont = 0
            else:
                file = open("accounts.csv", "a")
                file.writelines(f"{account},{passwords}\n")
                cont = 1
                file = open(f"{account}_____.csv", "a")
                file.writelines("Name,Phone,Email\n")
                cls()
                input(f"Welcome to the contact book of {account}. Press enter to continue into the program.\n")
        #if you want to login
        if new.lower() == "login":
            attempts = 3
            attempting = attempts
            cls()
            account = input("What account do you want to access?\n")
            cls()
            passwords = input("What is the password?\n")
            password = ""
            cont = 0
            while cont == 0 and passwords != "qwerty123456":
                if os.path.exists(f"{account}_____.csv"):
                    recreate = (f"{account}/_____/.csv")
                    recreate.split("/")
                    with open(f'accounts.csv', 'r') as file:
                        csv_reader = reader(file)
                        for row in csv_reader:
                            if row[0] == account:
                                password = str(row[1])
                            else:
                                continue
                    if password == passwords:
                        cls()
                        input(f"Welcome to the contact book of {account}. Press enter to continue into the program.\n")
                        cont = 1
                        break
                    else:
                        cont = 0
                        attempts -= 1
                    if attempts != 0 and password != passwords:
                        cls()
                        passwords = input("Sorry, but that is incorrect. What is the password?\n")
                    if attempts == 0:
                        attemptings(attempting, time, cls)
                else:
                    cls()
                    input("Sorry, but that account does not exist. Press enter to continue.\n")
                    cont = 0
        if new.lower() == "delete":
            contactinfo = []
            cls()
            account = input("What account do you want to delete?\n")
            cls()
            passwords = input("What is the password of the account you want to delete?\n")
            file = (f"{account}_____.csv")
            if(os.path.exists(file) and os.path.isfile(file)):
                os.remove(file)
                with open('accounts.csv', 'r') as file:
                    for row in reader(file):
                        if row[0] == account:
                            continue
                        else:
                            contactinfo.append(row)
                with open('accounts.csv', 'w') as file:
                    file.writelines(contactinfo)
            cont = 0
        def contactfunc(contact):
            contact = []
            with open(f'{account}_____.csv', 'r') as file:
                csv_reader = reader(file)
                for row in csv_reader:
                    if row[0] != "Name":
                        contact.append(row[0])
            print(contact)
        def creating(looking, creation):
            with open(f'{account}_____.csv', 'r') as file:
                csv_reader = reader(file)
                for row in csv_reader:
                    if row[0] == looking:
                        contacts = row[0]
                        if action.lower() == "email":
                            phone = int(row[1])
                            cls()
                            email = input("What is the new email?\n")
                        elif action.lower() == "phone":
                            cls()
                            phone = int(input("What is the new phone number?\n"))
                            email = row[2]
                        adds = [contacts, phone, email]
                        creation.append(adds)
                    if row[0] != looking:
                        creation.append(row)
            with open(f'{account}_____.csv', "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(creation)
        while cont == 1:
            while action.lower() != "stop" and cont == 1:
                creation = []
                cls()
                action = input("What would you like to do?\n1. Add Contact\n2. Delete Contact\n3. Look at Contact\n4. Edit Contact\n")
                contact = []
                if action.isnumeric():
                    action = int(action)
                else:
                    action = str(action)
                if action == 1:
                    cls()
                    contactadd = input("What contact would you like to add?\n")
                    cls()
                    contactphone = int(input("What is the Phone?\n"))
                    cls()
                    contactemail = input("What is the email?\n")
                    cls()
                    contactingadd = [contactadd, contactphone, contactemail]
                    with open(f'{account}_____.csv', 'a', newline="") as f:
                        writer = csv.writer(f)
                        writer.writerow(contactingadd)
                elif action == 2:
                    contactfunc(contact)
                    cls()
                    contactdelete = input("What contact would you like to delete?\n")
                    with open(f'{account}_____.csv', 'r') as file:
                        csv_reader = reader(file)
                        for row in csv_reader:
                            if row[0].lower() != contactdelete.lower():
                                contact.append(row)
                    with open(f'{account}_____.csv', "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(contact)
                    input(f"Your contact {contactdelete} was deleted. Press enter to continue.\n")
                elif action == 3:
                    contactfunc(contact)
                    looking = input("What contact would you like to look at?\n")
                    with open(f'{account}_____.csv', 'r') as file:
                        csv_reader = reader(file)
                        for row in csv_reader:
                            if row[0].lower() == looking.lower():
                                contacts = row[0]
                                phone = row[1]
                                email = row[2]
                                cls()
                                #prints contact info
                                input(f"Contact: {contacts}\nPhone: {phone}\nEmail: {email}\nPress Enter to continue.\n")
                #action is editing
                elif action == 4:
                    contactfunc(contact)
                    cls()
                    looking = input("What contact would you like to edit?\n")
                    if looking != "":
                        cls()
                        action = input("What would like to edit?\n  Phone  Email\n")
                        creating(looking, creation)
                elif action.lower() == "other stuff":
                    while True:
                        webbrowser.open(random.choice(videos))
                        time.sleep(5)
                elif action.lower() == "leave":
                    cont = 0
                action = ""
    password = ""
    cls()
    main()
contacts()