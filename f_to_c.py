def converter():
    import os
    def celsius(s):
        f = float(s)
        c = (f - 32) * 5/9
        return c
    def fahrenheit(s):
        c = float(s)
        f = (c/(5/9)) + 32
        return f
    os.system('cls')
    amount = int(input("What is the number you wish to convert?\n"))
    os.system('cls')
    changing = input("Would you like to change it to (f)ahrenheit or (c)elsius?\n")
    os.system('cls')
    if changing == "f":
        print(fahrenheit(amount))
    elif changing == "c":
        print(celsius(amount))
converter()