# Zadanie 6
# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę
# od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 5

guess = int(input("Zgadnij liczbe od 0 do 20: "))

while secret_num != guess:
    guess = int(input("Zgadnij liczbe od 0 do 20: "))

print("Zgadles!")    