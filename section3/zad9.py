# Zadanie 9
# W podanym przez użytkownika ciągu wejściowym policz
# wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

txt = str(input("Podaj wyraz: "))

lower_letters = 0
upper_letters = 0
numbers = 0
special_chars = 0

for i in txt:
    if i.islower():
        lower_letters += 1
    elif i.isupper():
        upper_letters += 1
    elif i.isdigit():
        numbers += 1
    else:
        special_chars += 1

print("Ilosc malych liter:", lower_letters)
print("Ilosc duzych liter:", upper_letters)
print("Ilosc cyfr:", numbers)
print("Ilosc znakow specjalnych:", special_chars)