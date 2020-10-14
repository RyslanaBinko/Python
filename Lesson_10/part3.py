def shift(list_of_num,step):
    if step < 0:
        step = abs(step)
        for i in range(step):
            list_of_num.append(list_of_num.pop(0))
    else:
        for i in range(step):
            list_of_num.insert(0,list_of_num.pop())


num = [1, 2, 3, 4, 5]
step = int(input("Enter the number for step: "))
shift(num, step)
print(num)