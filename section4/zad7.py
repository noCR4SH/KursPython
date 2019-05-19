# Zadanie 7
# Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
# (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.

names = str(input("Podaj imiona po spacji: "))

names_list = names.split()

for i in names_list:
    print("Hello", i)