names = str(input("Podaj imiona po spacji: "))

names_list = names.split()

for i in names_list:
    print("Hello", i)