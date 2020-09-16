def is_prime(num):
    d = 2
    while num % d != 0:
        d += 1
    return d == num

num = int(input("Enter number "))
if num > 0 and num < 1000:
    print(is_prime(num))
else:
    print("Wrong number")