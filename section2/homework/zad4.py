# Zadanie 4
# Dla liczb hex_num = 1DB i oct_num = 2063 zwróć wartość w systemie dziesiętynym.

hex_num = "1DB" #B = 11, D = 13
oct_num = "2063"

hex_to_int = int(hex_num, 16)
oct_to_int = int(oct_num, 8)

print("1DB =", hex_to_int)
print("2063 =", oct_to_int)