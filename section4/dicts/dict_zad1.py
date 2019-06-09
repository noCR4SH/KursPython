lists_to_dict = [[2, 4], [8, 9]]

dict_from_list = {}

for i in lists_to_dict:
    dict_from_list[i[0]] = i[1]

print(dict_from_list)