v = int(input("Cyclist speed is " ))
t = int(input("Travel time is "))
d = v*t
if v < 0:
    print("Vasia drove in the opposite direction ",abs(d), " km")
else:
    if d < 100 and d > 0:
        print("Vasia stopped at the mark ",d)
    else:
        print("Vasia reached the finish line")