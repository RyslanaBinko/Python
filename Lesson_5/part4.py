some_list = [3, 6, 8, 67, 45, 8, 65, 345, 10]
for i in range(len(some_list)):
    if some_list[i] % 2 != 0:
        some_list[i] = 0
print(some_list)
print("Count of zero ", some_list.count(0))
