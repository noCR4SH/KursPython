input_list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

part1 = len(input_list)//3
part2 = part1 * 2
part3 = part1 * 3

list_1 = input_list[:part1]
list_2 = input_list[part1:part2]
list_3 = input_list[part2:part3]

list_1.reverse()
list_2.reverse()
list_3.reverse()

print(list_1)
print(list_2)
print(list_3)