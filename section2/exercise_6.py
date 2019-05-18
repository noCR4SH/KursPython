# Zadanie 6
# Zarówno lodowka, jak i winda maja wysokosc, szerokosc i glebokosc. 
# Dowiedz sie, ile miejsca pozostalo w windzie, gdy lodowka jest w srodku.
# Zalozmy, ze wymiary lodowki zawsze beda mniejsze niz windy ( jest to prawdopodobne?)
# Wejscie i wyjscie powinny byc zrozumiale dla uzytkownika.

fridge_width = float(input("Podaj szerokosc lodowki: "))
fridge_depth = float(input("Podaj glebokosc lodowki: "))
fridge_height = float(input("Podaj wysokosci lodowki: "))

lift_width = float(input("Podaj szerokosc windy: "))
lift_depth = float(input("Podaj glebokosc windy: "))
lift_height = float(input("Podaj wysokosci windy: "))

fridge_volume = fridge_width * fridge_depth * fridge_height
lift_volume = lift_width * lift_depth * lift_height

if fridge_volume < lift_volume:
    print("W windzie pozostalo", lift_volume - fridge_volume, "miejsca")
else:
    print("Proponuje schowac winde do lodowki")