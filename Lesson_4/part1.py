x = float(input("km in first day "))
y = int(input("number of km "))
day = 1
sum_km = x
while sum_km < y:
    x = x + (0.1 * x)
    day = day + 1
    sum_km = sum_km + x
print("The athlete ran ", y, " km in ", day, " days")

