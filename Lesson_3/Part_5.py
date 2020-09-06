import random
a = 1
while a <= 3:
    num = int(input("Enter your number "))
    while num < 1 or num > 10:
        num = int(input("Wrong number. Enter another number "))
    rand = random.randint(1, 10)
    if num == rand:
        print("You won!")
        break
    else:
        print("You lose!")
    a = a + 1

