fuel_consumption = 6.4 #liters per 100KM
cost_per_liter = 5.04
trip = 120

cost = fuel_consumption * trip/100 * cost_per_liter

print("It will cost", cost, "PLN.")