# Zadanie 3
# Dla podanej liczby w systemie dwójkowym bin_num = 1001111 oblicz wartość w systemie dziesiętnym.
# Zamianę z systemu binarnego na dziesiętny napisz samodzielnie (nie korzystaj z metody wbudowanej).

bin_num = 1001111
bin_to_str = str(bin_num)

bin_to_dec = int(bin_to_str[-1]) * 1 + int(bin_to_str[-2]) * 2 + int(bin_to_str[-3]) * 4 + int(bin_to_str[-4]) * 8 + int(bin_to_str[-7]) * 64

print(bin_to_dec)