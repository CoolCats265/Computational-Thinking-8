while True:
    word = input("What do you think grandma likes? ")

    if len(word) < 10 or "o" in word:
        print(f"Grandma doesn't like {word} ")

    else:
        print(f"Grandma likes {word}!")

        print("")