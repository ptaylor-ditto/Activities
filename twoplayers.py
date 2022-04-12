def player2(p1cards, p2cards, random, os):
    playerone = []
    playertwo = []
    while len(p1cards) + len(playerone) > 0 and len(p2cards) + len(playertwo) > 0:
        #battle cards
        if len(p1cards) == 0:
            p1cards.append(playerone)
            playerone = []
        if len(p2cards) == 0:
            p2cards.append(playertwo)
            playertwo = []
        p1play = random.choice(p1cards)
        p1cards.remove(p1play)
        p2play = random.choice(p2cards)
        p2cards.remove(p2play)
        #finding numbers in cards
        p1number = p1play.translate({ord(i): None for i in 'abdefilmnoprstuCDHS'})
        print(p1number)
        p2number = p2play.translate({ord(i): None for i in 'abdefilmnoprstuCDHS'})
        print(p2number)
        #determines which is higher
        if p1number > p2number:
            playerone.append(p1play)
            playerone.append(p2play)
            input(f"Player 1 won the battle. They gained the the {p1play} and the {p2play}.\n")
        elif p2number > p1number:
            playertwo.append(p1play)
            playertwo.append(p2play)
            input(f"Player 2 won the battle. They gained the {p1play} and the {p2play}.\n")
        else:
            playerone.append(p1play)
            playertwo.append(p2play)
            input(f"There was a tie between the {p1play} and the {p2play}. The cards were returned to the decks.\n")
        os.system('cls')
    #Who won?
    if len(p1cards) == 0:
        print("Congratulations, Player 2. You won the Game of War.")
    if len(p2cards) == 0:
        print("Congratulations Player 1. You won the Game of War.")
    return p1cards, p2cards