num1 = int(input("Podaj pierwsza liczbe: "))
num2 = int(input("Podaj druga liczbe: "))
num3 = int(input("Podaj trzecia liczbe: "))

def minimum_of(a, b, c):
    if a < b and a < c:
        return a;
    elif b < a and b < c:
        return b
    else:
        return c


minimum = minimum_of(num1, num2, num3)

print(minimum)