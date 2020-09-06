num = int(input("Enter your number "))
a = 1
b = 1
while a <= num:
    b = a * b
    a = a + 1
print(b)