# Zadanie 2
# Zmodyfikuj skrypt zad1.py tak, by przyjmował wartości od użytkownika



fuel_consumption = float(input("Podaj spalanie na 100KM: ")) #liters per 100KM
cost_per_liter = float(input("Podaj obecna cene paliwa: "))
trip = int(input("Podaj dlugosc trasy: "))

cost = fuel_consumption * trip/100 * cost_per_liter

print("Trasa bedzie cie kosztowala", round(cost, 2), "PLN.")