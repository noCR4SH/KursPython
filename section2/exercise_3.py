# Zadanie 3
# Napisz skrypt, ktory pozwala wprowadzic 4 liczby calkowite, dodac je i wyswietl wynik na ekranie.
# Wejscie i wyjscie powinny byc zrozumiale dla uzytkownika.

print("------------------ Sumowanie liczb ------------------")
print("Program pyta uzytkownika o 4 dowolne liczby calkowite")
print("a nastepnie zwraca ich sume.")

num1 = int(input("Podaj pierwsza liczbe: "))
num2 = int(input("Podaj druga liczbe: "))
num3 = int(input("Podaj trzecia liczbe: "))
num4 = int(input("Podaj czwarta liczbe: "))

sum = num1 + num2 + num3 + num4

print("Suma liczb wynosi:", sum)