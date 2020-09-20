string = str(input("Enter the text: "))

def word_in_text(func):
    def text():
        print(string)
        func()
    return text()


@word_in_text
def list_of_the_word():
    print(string.split(' '))
