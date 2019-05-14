# Zadanie 1
# Napisz skrypt, który oblicza ile minut ma rok

hours_per_day = 24
minutes_per_hour = 60

minutes_per_year = 365 * hours_per_day * minutes_per_hour
minutest_per_leap_year = 366 * hours_per_day * minutes_per_hour

print("Minutes per year: " + str(minutes_per_year))
print("Minutes per leap year: " + str(minutest_per_leap_year))