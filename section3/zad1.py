# Zadanie 1
# Oblicz koszt wyprawy znając dystans, spalanie na 100km i cene litra benzyny.
# Załóż, że spalanie na 100km wynosi 6,4 l,
# trasa to 120km,
# litr benzyny kosztuje 5,04 zł.

fuel_consumption = 6.4 #liters per 100KM
cost_per_liter = 5.04
trip = 120

cost = fuel_consumption * trip/100 * cost_per_liter

print("It will cost", cost, "PLN.")