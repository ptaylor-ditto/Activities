def player1(p1cards, cpucards, random, os):
    playerone = []
    computer = []
    while len(p1cards) + len(playerone) > 0 and len(cpucards) + len(computer) > 0:
        #battle cards
        if len(p1cards) == 0:
            p1cards.append(playerone)
            playerone = []
        if len(cpucards) == 0:
            cpucards.append(computer)
            computer = []
        p1play = random.choice(p1cards)
        p1cards.remove(p1play)
        cpuplay = random.choice(cpucards)
        cpucards.remove(cpuplay)
        #finding numbers in cards
        p1number = p1play.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'})
        print(p1number)
        cpunumber = cpuplay.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'})
        print(cpunumber)
        #determines which is higher
        if p1number > cpunumber:
            playerone.append(p1play)
            playerone.append(cpuplay)
            input(f"You won the battle. You gained the the {p1play} and the {cpuplay}.\n")
        elif cpunumber > p1number:
            computer.append(p1play)
            computer.append(cpuplay)
            input(f"The computer won the battle. They gained the {p1play} and the {cpuplay}.\n")
        else:
            playerone.append(p1play)
            computer.append(cpuplay)
            input(f"There was a tie between the {p1play} and the {cpuplay}. The cards were returned to the decks.\n")
        os.system('cls')
    #Who won?
    if len(p1cards) == 0:
        print("I'm sorry, but the computer won this game of war.")
    if len(cpucards) == 0:
        print("Congratulations. You won the game of war.")