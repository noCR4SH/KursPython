# Zadanie 4
# Napisz skrypt, który zapyta uzytkownika o trzy liczby calkowite,
# a nastepnie pomnoz dwa pierwsze. przed podzieleniem wyniku przez trzecia liczbe. 
# Wejscie i wyjscie powinny byc zrozumiale dla uzytkownika.

num1 = int(input("Podaj pierwsza liczbe: "))
num2 = int(input("Podaj druga liczbe: "))
num3 = int(input("Podaj trzecia liczbe: "))

result = num1 * num2 / num3

print("Wynik wynosi:", result)