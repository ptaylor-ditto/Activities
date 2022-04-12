def blackjack():
    import random, os
    def cls():
        os.system('cls')
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    deck = []
    playercards = []
    dealercards = []
    playerscore = 0
    dealerscore = 0
    pcard = ""
    dcard = ""
    choices = [11, 1]
    def playerdraw():
        pcard = random.choice(deck)
        playercards.append(pcard)
        deck.remove(pcard)
    def dealerdraw():
        dcard = random.choice(deck)
        dealercards.append(dcard)
        deck.remove(dcard)
    def numbering():
        pnumber = pcard.translate({ord(i): None for i in 'abdefilmnoprstuCDHS'})
        playerscore = playerscore + pnumber
        dnumber = dcard.translate({ord(i): None for i in 'abdefilmnoprstuCDHS'})
        dealerscore = dealerscore + dnumber
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')
    random.shuffle(deck)
    while len(playercards) != 2 and len(dealercards) != 2:
        playerdraw()
        dealerdraw()
        numbering()
    cls()
    playerscore = 0
    dealerscore = 0
    hs = int(input(f"Player Score: {playerscore}\nDealer Score: {dealerscore}\n1. Hit\n2. Stand\n"))
    while playerscore < 22 and dealerscore < 22:
        while hs != 1 and hs != 2:
            hs = int(input(f"Player Score: {playerscore}\nDealer Score: {dealerscore}\n1. Hit\n2. Stand\n"))
        playerdraw()
        dealerdraw()
        numbering()