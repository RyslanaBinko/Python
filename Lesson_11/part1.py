win = int(input("win count: "))
draw = int(input("draw count: "))
loss = int(input("loss count: "))


def points_count():
    count_points = (win * 3) + draw
    print(count_points)


points_count()
