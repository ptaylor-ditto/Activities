def countdown():
    import time, os
    def cls():
        os.system('cls')
    cls()
    unit = input("What measurement of time would you like to count down in(seconds, minutes, hours)?\n")
    cls()
    amount = int(input(f"How many {unit} would you like to count down?\n"))
    cls()
    countdown = input("What would you like to countdown in(seconds, actual)?\n")
    if countdown.lower() == "seconds":
        if unit == "seconds":
            seconds = amount
        elif unit == "minutes":
            seconds = amount*60
        elif unit == "hours":
            seconds = amount*1200
        while seconds > 0:
            cls()
            print(f'{seconds} seconds')
            time.sleep(1)
            seconds -= 1
    elif countdown.lower() == "actual":
        if unit == "seconds":
            for x in amount:
                cls()
                print(f'{seconds} seconds')
                time.sleep(1)
                seconds -= 1
        elif unit == "minutes":
            minutes = amount
            for x in range(0, minutes):
                seconds = 60
                cls()
                print(f'{minutes} minutes')
                time.sleep(1)
                minutes -= 1
                if minutes != 0:
                    for x in range(0, 60):
                        cls()
                        print(f'{minutes} minutes, {seconds} seconds')
                        time.sleep(1)
                        seconds -= 1
                else:
                    for x in range(0, 60):
                        cls()
                        print(f'{seconds} seconds')
                        time.sleep(1)
                        seconds -= 1
        elif unit == "hours":
            hours = amount
            for x in range(0, hours):
                cls()
                print(f'{hours} hours')
                time.sleep(1)
                hours -= 1
                minutes = 59
                for x in range(0, 60):
                    minutes = 59
                    hours -= 1
                    seconds = 59
                    if hours != 0:
                        if minutes != 0:
                            for x in range(0, 60):
                                cls()
                                print(f'{hours} hours, {minutes} minutes, {seconds} seconds')
                                time.sleep(1)
                                seconds -= 1
                        else:
                            for x in range(0, 60):
                                cls()
                                print(f'{hours} hours, {seconds} seconds')
                                time.sleep(1)
                                seconds -= 1
                    else:
                        if minutes != 0:
                            for x in range(0, 60):
                                cls()
                                print(f'{minutes} minutes, {seconds} seconds')
                                time.sleep(1)
                                seconds -= 1
                        else:
                            for x in range(0, 60):
                                cls()
                                print(f'{seconds} seconds')
                                time.sleep(1)
                                seconds -= 1
countdown()