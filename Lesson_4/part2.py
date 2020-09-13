#num = int(input("Enter your number "))
#if num == 0:
    #break
#elif num < 0:
    #print("Wrong number! Enter another number ")
sum = 0
multip = 1
count = 0
maximum = 0
max_id = 0
max_count = 0
second_large = 0
average = 0
even = 0
odd = 0
while True:
    num = int(input("Enter number "))
    if num == 0:
        break
    elif num < 0:
        print("Wrong number! Enter another number ")
    else:
        sum = sum + num
        multip = multip * num
        count += 1
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        if num > maximum:
            second_large = maximum
            maximum = num
            max_id = count
            max_count = 1
        elif num == maximum:
            max_count += 1
        elif num < maximum and num > second_large:
            second_large = num
        average = sum / count
print("\n", "summa ", sum, "\n", "multiply ", multip, "\n", "count ", count, "\n", "maximum ", maximum, "\n",\
"max id ", max_id, "\n", "average ", average, "\n", "max count ", max_count, "\n",\
"second large ", second_large, "\n", "even ", even, "\n", "odd ", odd)