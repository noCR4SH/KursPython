# Zadanie 4
# Napisz program, który wyświetli kolejne wyniki dla silnii liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).
result = 1

n = int(input("Podaj n, nie wieksze niz 8: "))

if n <= 8:
    for i in range(1, n+1):
        result *= i
        print(result)
else:
    print("Za duza liczba!")
