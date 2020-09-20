t = float(input("Enter temperature "))
t_type = input("Enter temperature type - C,F or K: ")
if t_type == "C":
    c_in_k = t + 273.15
    c_in_f = (9 / 5.0 * t) + 32
    print("Temp in C = ", t)
    print("Temp in F = ", c_in_f)
    print("Temp in K = ", c_in_k)
elif t_type == "K":
    k_in_c = t - 273.15
    k_in_f = -457.87 * t
    print("Temp in K = ", t)
    print("Temp in C = ", k_in_c)
    print("Temp in F = ", k_in_f)
else:
    f_in_c = 5.0 * (t - 32) / 9
    f_in_k = (t + 459.67) * 5 / 9
    print("Temp in F = ", t)
    print("Temp in C = ", f_in_c)
    print("Temp in K = ", f_in_k)