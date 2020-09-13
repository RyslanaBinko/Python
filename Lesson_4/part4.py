num = int(input("Enter your number "))
step = 1
if num <= 9 and num > 0:
    while step <= num:
        print(*range(1, step + 1), sep="")
        step += 1