import re


class Password:
    def __init__(self, passw):
        self.__passw = passw
        self.__find_upper = re.findall(r'([A-Z])', passw)
        self.__find_small = re.findall(r'([a-z])', passw)
        self.__find_num = re.findall(r'([0-9])', passw)
        self.__find_symb = re.findall(r'([$#@\-+=*_&?])', passw)
        self.__check = True

    def pass_check(self):
        if len(self.__passw) >= 8:
            if self.__find_upper:
                if self.__find_small:
                    if self.__find_num:
                        if self.__find_symb:
                            print("Password is correct")
                            self.__check = False
                        else:
                            print("Missing symbol")
                    else:
                        print("Missing number")
                else:
                    print("Missing small letter")
            else:
                print("Missing upper letter")
        else:
            print("Wrong password lenght")
        return self.__check


check = True
while check:
    password = input("Enter your password: ")
    passw = Password(password)
    check = passw.pass_check()
