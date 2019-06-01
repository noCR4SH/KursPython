multi_table = []

for i in range(1, 11):
    multi_table.append([])
    for n in range(1, 11):
        multi_table[i-1].append(i * n)


for j in range(len(multi_table)):
    print(multi_table[j])