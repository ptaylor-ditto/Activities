def spellcheck():
    from textblob import TextBlob
    import os
    words = []
    os.system('cls')
    add_word = input("What is the incorrectly spelled word (input '123' to stop)?\n")
    words.append(add_word)
    while add_word != "123":
        os.system('cls')
        add_word = input("What is the incorrectly spelled word (input '123' to stop)?\n")
    corrected_words = []
    for i in words:
        corrected_words.append(TextBlob(i))
    os.system('cls')
    print("Wrong words :", words)
    print("Corrected Words are :")
    for i in corrected_words:
        print(i.correct(), end="\n")
spellcheck()