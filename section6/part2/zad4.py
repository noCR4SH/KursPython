def check_num(min, max, n):
    if n < max and n > min:
        print("Tak, liczba", n, "znajduje sie w zadanym zakresie")
    else:
        print("Nie, liczba", n, "jest z poza zakresu")

minimum = int(input("Podaj poczatek zakresu: "))
maximum = int(input("Podaj koniec zakresu: "))

num = int(input("Podaj liczbe: "))

check_num(minimum, maximum, num)