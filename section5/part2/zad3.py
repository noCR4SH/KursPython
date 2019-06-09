num1 = int(input("Podaj pierwsza liczbe: "))
num2 = int(input("Podaj druga liczbe: "))
num3 = int(input("Podaj trzecia liczbe: "))

def max_of(a, b, c):
    if a > b and a > c:
        return a;
    elif b > a and b > c:
        return b
    else:
        return c


maximum = max_of(num1, num2, num3)

print(maximum)