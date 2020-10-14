some_text = "Marvel makes good movies, DC makes good comics"

def text_replacement(x, y, i):
    repl = some_text.replace(x, y, i)
    print(repl)

text_replacement("Marvel", "DC", 1)