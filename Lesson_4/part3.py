num_first = int(input("Enter first number "))
num_second = int(input("Enter second number "))
if num_first <= num_second:
    while num_first <= num_second:
        print(num_first)
        num_first += 1
else:
    while num_first >= num_second:
        print(num_first)
        num_first -=1