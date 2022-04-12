def war():
    import random, time, os
    from oneplayer import player1
    from twoplayers import player2
    os.system('cls')
    while True:
        os.system('cls')
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        p1cards = []
        cpucards = []
        p2cards = []
        deck = []
        players = input("Are there one or two players? ")
        os.system('cls')
        print("Welcome to the Game of War.")
        time.sleep(2)
        os.system('cls')
        #creating the deck
        for suit in suits:
            for rank in ranks:
                deck.append(f'{rank} of {suit}')
        random.shuffle(deck)
        #dealing the deck
        deckstatus = ""
        if players == "1" or players.lower() == "one":
            while len(deck) > 1:
                card = random.choice(deck)
                deck.remove(card)
                p1cards.append(card)
                card = random.choice(deck)
                deck.remove(card)
                cpucards.append(card)
            player1(p1cards, cpucards, random, os)
        if players == "2" or players.lower() == "two":
            while len(deck) > 1:
                card = random.choice(deck)
                deck.remove(card)
                p1cards.append(card)
                card = random.choice(deck)
                deck.remove(card)
                p2cards.append(card)
        if players == "2":
            player2(p1cards, p2cards, random, os)
        if players.lower() == "leave":
            break
    #Saying goodbye... for now
    print("You have finished the game.\nGoodbye.")
war()