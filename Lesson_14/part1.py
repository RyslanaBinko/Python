import re

car_number = input("Enter the number: ").upper()
find = re.findall(r'([A-ZА-ЯІ]{2}\d{4}[A-ZА-ЯІ]{2})', car_number)
rus_reg = ["AA", "AB", "AC", "AE", "АН", "АМ", "АО", "АР", "АТ", "АК", "АІ", "ВА", "ВВ", "ВС", "ВЕ",
           "ВН", "ВІ", "ВК", "ВМ", "ВО", "АХ", "ВТ", "ВХ", "СА", "СВ", "СЕ", "СН", "ІІ"]

eng_reg = ["AA", "AB", "AC", "AE", "AH", "AM", "AO", "AP", "AT", "AK", "AI", "BA", "BB", "BC", "BE",
           "BH", "BI", "BK", "BM", "BO", "AX", "BT", "BX", "CA", "CB", "CE", "CH", "II"]

reg_name = ["г. Киев", "Винницкая обл.", "Волынская обл.", "Днепропетровская обл.",
            "Донецкая обл.", "Житомирская обл.", "Закарпатская обл.", "Запорожская обл.",
            "Ивано-Франковская обл.", "АР Крым", "Киевская обл.", "Кировоградская обл.",
            "Луганская обл", "Львовская обл.", "Николаевская обл.", "Одесская обл.",
            "Полтавская обл.", "Ровенская обл.", "Сумская обл.", "Тернопольская обл.",
            "Харьковская обл.", "Херсонская обл.", "Хмельницкая обл.",
            "Черкасская обл.", "Черниговская обл.", "Черновицкая обл.",
            "г. Севастополь", "Общегосударственная"]
d_rus = dict(zip(rus_reg, reg_name))
d_eng = dict(zip(eng_reg, reg_name))

if find:
    print("Your car number is ", find)
    region = find[0][:2]

    if region in d_rus.keys():
        print(d_rus[region])
    elif region in d_eng.keys():
        print(d_eng[region])
    else:
        print("Unknown region")

else:
    print("wrong number format")