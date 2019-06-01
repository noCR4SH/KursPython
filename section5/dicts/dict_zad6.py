days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

dict_to_list = list(days.values())
list_days = []

for i in dict_to_list:
    if i not in list_days:
        list_days.append(i)

print(list_days)