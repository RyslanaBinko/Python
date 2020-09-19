parameter = input("Enter parameter ")
side_1 = int(input("Enter first side "))
side_2 = int(input("Enter second side "))

def area (x: int, y: int, parameter: "square"):
    if parameter == "square":
        s = side_1 ** 2
        return s
    else:
        s = 0.5 * side_1 * side_2
        return s

print(area(side_1,side_2,parameter))



