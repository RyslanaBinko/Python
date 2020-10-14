fname = "your_text"
f = open(fname, "w")
while True:
    st = input()
    if st == "":
        break
    f.write(st + "\n")
f.close()