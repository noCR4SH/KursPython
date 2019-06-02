def is_even(n):
    if n % 2 == 0:
        return "Liczba jest parzysta"
    else:
        return "Liczba nie jest parzysta"

num = int(input("Podaj liczbe: "))

print(is_even(num))