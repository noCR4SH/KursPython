# Zadanie 7
# Napisz konwerter walut.
# Program poprosi uzytkownika o kwote pieniedzy, jaka wezma na wakacje
# a nastepnie przeliczy te kwote w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknac z konwersji.
# Wejscie i wyjscie powinny być zrozumiale dla uzytkownika.

budget = float(input("Podddaj swoj budzet: "))

euro_budget = budget / 4.30
dollar_budget = budget / 3.85

print("Posiadasz", round(euro_budget, 2), "euro")
print("Posiadasz", round(dollar_budget, 2), "dolarow")