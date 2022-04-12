def hearts():
    import random, os
    restart = "yes"
    while restart.lower() == "yes":
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        p1cards = []
        p2cards = []
        p3cards = []
        p4cards = []
        deck = []
        played = []
        players = int(input("How many players are there?\n"))
        os.system('cls')
        #creating the deck
        for suit in suits:
            for rank in ranks:
                deck.append(f'{rank} of {suit}')
        random.shuffle(deck)
        #dealing the deck
        while len(deck) > 3:
            card = random.choice(deck)
            deck.remove(card)
            p1cards.append(card)
            card = random.choice(deck)
            deck.remove(card)
            p2cards.append(card)
            card = random.choice(deck)
            deck.remove(card)
            p3cards.append(card)
            card = random.choice(deck)
            deck.remove(card)
            p4cards.append(card)
        while len(p1cards) > 0 and len(p2cards) > 0 and len(p3cards) > 0 and len(p4cards) > 0:
            #choosing the cards
            os.system('cls')
            print(p1cards)
            p1play = input("P1, choose your card.\n")
            p1play = p1play.lower()
            if p1cards.count(p1play) >= 1:
                p1cards.remove(p1play)
                played.append(p1play)
            elif p1play.lower() == "leave":
                break
            if  players > 1:
                os.system('cls')
                print(p2cards)
                p2play = input("P2, choose your card.\n")
                p2play = p2play.lower()
                if p2cards.count(p2play) >= 1:
                    p2cards.remove(p2play)
                    played.append(p2play)
                elif p2play.lower() == "leave":
                    break
            else:
                p2play = random.choice(p2cards)
                p2cards.remove(p2play)
                played.append(p2play)
            if players > 2:
                os.system('cls')
                print(p3cards)
                p3play = input("P3, choose your card.\n")
                p3play = p3play.lower()
                if p3cards.count(p3play) >= 1:
                    p3cards.remove(p3play)
                    played.append(p3play)
                elif p3play.lower() == "leave":
                    break
            else:
                p3play = random.choice(p3cards)
                p3cards.remove(p3play)
                played.append(p3play)
            if players > 3:
                os.system('cls')
                print(p4cards)
                p4play = input("P4, choose your card.\n")
                p4play = p4play.lower()
                if p4cards.count(p4play.lower()) >= 1:
                    p4cards.remove(p4play)
                    played.append(p4play)
                elif p4play.lower() == "leave":
                    break
            else:
                p4play = random.choice(p4cards)
                p4cards.remove(p4play)
                played.append(p4play)
            #finding numbers in cards
            p1number = p1play.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'})
            print(p1number)
            p2number = p2play.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'})
            print(p2number)
            p3number = p3play.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'})
            print(p3number)
            p4number = p4play.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'})
            print(p4number)
            played = []
            #determines which is higher
            if p1number > p2number and p1number > p3number and p1number > p4number:
                p1cards.append(p1play)
                p1cards.append(p2play)
                p1cards.append(p3play)
                p1cards.append(p4play)
                leaving = input(f"Player 1, you won the battle. You gained the {p1play}, the {p2play}, the {p3play}, and the {p4play}.\n")
            elif p2number > p1number and p2number > p3number and p2number > p4number:
                p2cards.append(p1play)
                p2cards.append(p2play)
                p2cards.append(p3play)
                p2cards.append(p4play)
                leaving = input(f"Player 2, you won the battle. You gained the {p1play}, the {p2play}, the {p3play}, and the {p4play}.\n")
            elif p3number > p1number and p3number > p2number and p3number > p4number:
                p3cards.append(p1play)
                p3cards.append(p2play)
                p3cards.append(p3play)
                p3cards.append(p4play)
                leaving = input(f"Player 3, you won the battle. You gained the {p1play}, the {p2play}, the {p3play}, and the {p4play}.\n")
            elif p4number > p1number and p4number > p2number and p4number > p3number:
                p4cards.append(p1play)
                p4cards.append(p2play)
                p4cards.append(p3play)
                p4cards.append(p4play)
                leaving = input(f"Player 4, you won the battle. You gained the {p1play}, the {p2play}, the {p3play}, and the {p4play}.\n")
            else:
                p1cards.append(p1play)
                p2cards.append(p2play)
                p3cards.append(p3play)
                p4cards.append(p4play)
                leaving = input(f"There was a tie. The cards were returned to the decks.\n")
            os.system('cls')
            if leaving.lower() == "leave":
                break
        #Who won?
        if len(p1cards) == 0:
            print("Sorry Player 1, you lost.")
        if len(p2cards) == 0:
            print("Sorry Player 2, you lost.")
        if len(p3cards) == 0:
            print("Sorry Player 3, you lost.")
        if len(p4cards) == 0:
            print("Sorry Player 4, you lost.")
        restart = input("Would you like to play again?")
        os.system('cls')
    #Saying goodbye... for now
    print("You have finished the game.\nGoodbye.")
hearts()