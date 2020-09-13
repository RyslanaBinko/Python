string = input("Enter your string ")
print("third symbol is ", string[2], "\n", "penult ", string[len(string) - 2], "\n", "first five symbols ", string[0:5], "\n",\
"without the last two ", string[0:-2], "\n", "odd symbols ", string[1::2], "\n", "even symbols ", string[::2], "\n",\
"in revers order ", string[::-1], "\n", "in revers order in one ", string[::-2], "\n", "length of string ", len(string))
