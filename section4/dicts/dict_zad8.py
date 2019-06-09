uk_names = ["Olivia", "Amelie", "Isla", "Ava", "Emily", "Isabella", "Mia", "Poppy", "Ella", "Lily"]
germany_names = ["Mia", "Emma", "Sophia", "Hannah", "Emily", "Anna", "Marie", "Mila", "Amelie", "Lilly"]
italy_names = ["Sophia", "Emma", "Nicole", "Emily", "Rebecca", "Mia", "Adele", "Irene", "Arianna", "Viola"]
france_names = ["Emma", "Chloe", "Louise", "Sarah", "Anna", "Adele", "Sophia", "Mila", "Camille", "Julia"]
spain_names = ["Maria", "Sophia", "Julia", "Emma", "Valentina", "Anna", "Claudia", "Elsa", "Angela", "Eva"]

final_list = []
final_list.extend(uk_names)
final_list.extend(germany_names)
final_list.extend(italy_names)
final_list.extend(france_names)
final_list.extend(spain_names)

frequent_names = []

for i in final_list:
    if final_list.count(i) >= 3 and i not in frequent_names:
        frequent_names.append(i)

print("Frequent names in Europe: ")
for n in frequent_names:
    print(n)