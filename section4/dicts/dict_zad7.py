example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

clean_list = []

for i in example_list:
    if i not in clean_list:
        clean_list.append(i)

tuple_from_list = tuple(clean_list)

print("Max value =", max(tuple_from_list))
print("Min value = ", min(tuple_from_list))