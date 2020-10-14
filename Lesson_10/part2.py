word = input("Enter your word: ")


def palindrom(word):
    if word == word[::-1]:
        print("Your word " + word + " is palindrom")
    else:
        print("Your word " + word + " is not palindrom")


palindrom(word)