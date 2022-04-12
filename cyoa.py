def cyoa():
    import os, time
    while True:
        os.system('cls')
        choice1 = int(input("You arrive at a murder scene.\nDo you (1)stay, or (2)leave?\n"))
        if choice1 == 1:
            os.system('cls')
            choice2 = int(input("\nYou stay and notice something wierd. The police officer seems to be changing shape.\nDo you (1)walk up to the officer, or (2)stay in the shadows to watch?\n"))
            if choice2 == 1:
                os.system('cls')
                choice3 = int(input("\nAs you walk up, you notice the officer turned into a dragon. Then, the officer turns around.\nDo you (1)try to hide, or (2)talk to him?\n"))
            if choice3 == 1:
                os.system('cls')
                choice4 = int(input("\nAs you hide, the dragon turns around. He looks around and stops staring at the spot where you are.\nDo you (1) run away, or (2) stay put hoping he won't notice you?\n"))
                if choice4 == 1:
                    os.system('cls')
                    input("\nYou run away, hoping the dragon doesn't notice. You are lucky. He turned around right as you start running. You run with all of your strength. You are so close to your house. You turn around to see the dragon's snout peeking from behind the wall. You make it to your house. As you shut the door. You hear a roar. You peek from behind the curtains and see the dragon flying past, scanning the road and sidewalk for you. You escaped the dragon. Congratulations!!!!\n")
                    input("YOU SURVIVED!!!!!!!!!!!!!!!!!!!!!")
                if choice4 == 2:
                    os.system('cls')
                    input("\nAs you stay hidden the dragon turns around and walks away.\n\nCongratulations!!!! You survived your first encounter with a dragon!\n\n\n\n\n\nUnless it wasnt, bum bum buuuuuuum!!")
            if choice3 == 2:
                os.system('cls')
                input("You start talking. He looks confused at first, wondering why you are talking to him. Then, he gets over the confusion. He looks right into your eyes and opens his mouth. Too late, you turn around and start running. You feel a big blast of burning, scorching air behind you.\n\nYOU DIED!!!")
            elif choice2 == 2:
                os.system('cls')
                choice3 = int(input("\nAs you watch, the cop (now dragon) turns around. He starts staring at the spot where you are hiding.\nDo you (1)run away, or (2)stay put hoping he won't notice you?\n"))
            if choice3 == 1:
                os.system('cls')
                input("\nAs you run away, you feel a big wave of heat coming toward you. You sprint with all of your strength. You look behind you. You see that the dragon is keeping pace with you. With your last and final burst of strength, you try to reach the water, hoping to dissuade him. It doesn't work. He breathes white fire on the water, turning it to smoke. Then, he breathes it on you. You don't even have time to process the heat or pain before you turn to ash.\n\nYOU DIED!!")
            elif choice3 == 2:
                os.system('cls')
                choice4 = int(input("\nWhile hiding behind the wall, you notice that it is now so quiet you can hear yourself breathing. You peek out from behind the wall. You don't see the dragon anywhere.\nAre you (1)excited, or (2)scared?\n"))
                if choice4 == 1:
                    os.system('cls')
                    input("You sneak out from behind the wall only to get blasted with blue flames. You barely have time to process the pain and the fact that the police officer was hiding behind the other side of the wall before you fall to the ground and turn into ash.\n\nYOU DIED!")
                elif choice4 == 2:
                    os.system('cls')
                    input("You turn around, only to find that the dragon has found you.\n\nYOU DIED!!!")
        elif choice1 == 2:
            os.system('cls')
            input("\nAs you turn around, you feel a big wave of heat behind you. As you turn back around, you fall to the ground.\n\nYOU DIED!")
        else:
            os.system('cls')
            input("Sorry, I don't understand that choice.")
        os.system('cls')
        restart = input("Do you want to restart?\n¯\_(ツ)_/¯\n")
        if restart == "yes":
            continue
        elif restart == "f u":
            input("Keep it PG here")
            break
        else:
            os.system('cls')
            break
cyoa()