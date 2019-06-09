tuples_to_dict = ((2, 7), (5, 3))

dict_from_tuples = {}

for i in tuples_to_dict:
    dict_from_tuples[i[0]] = i[1]

print(dict_from_tuples)