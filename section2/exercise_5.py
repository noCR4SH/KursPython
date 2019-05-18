# Zadanie 5
# Napisz program, ktory pyta uzytkownika o 2 liczby
# a nastepnie dzieli jedna przez druga.
# Pokaz ile razy pierwsza liczba miesci sie w drugiej
# oraz jaka jest reszta tego dzielenia. 

num1 = int(input("Podaj pierwsza liczbe: "))
num2 = int(input("Podaj druga liczbe: "))

result = num1 / num2
result2 = num2 / num1
result3 = num2 % num1

print("Wynik dzielenia pierwszej liczy przez druga:", result)
print("Pierwsza liczba miesci sie w drugiej", int(result2), "razy.")
print("Reszta z dzielenia wynosi:", result3)