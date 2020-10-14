st = input("Enter your text ")


def long_word(st):
    n = max(st.split(), key=len)
    print(n)


long_word(st)