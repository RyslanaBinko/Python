import re

phone_number = input("Enter your phone number: ")


def format_num(number):
    format_number = (re.sub(r'(\d{3})(\d{3})(\d\d)(\d\d)', r'(+38) \1 \2-\3-\4', number))
    return format_number


def ph_number(number):
    number = "".join(filter(str.isdigit, phone_number))
    if len(number) == 12:
        if re.match(r'38', number):
            number = number[2:]
            return format_num(number)
        else:
            return "wrong number format"
    elif len(number) == 10:
        return format_num(number)
    else:
        return "wrong number format"


print(ph_number(phone_number))
