

def get_items():
    item_list = []

    print("Podaj 4 przedmioty: ")

    for i in range(4):
        item = input(str(i+1) + ": ")
        item_list.append(item)

    return item_list

def merge_lists(list1, list2, list3):
    merged_list = []
    merged_list.extend(list1)
    merged_list.extend(list2)
    merged_list.extend(list3)

    normalized_list = [x.lower() for x in merged_list]

    return normalized_list

def most_popular(item_list):
    counter = 0
    frequent = item_list[0]

    for i in item_list:
        frequency = final_list.count(i)
        if frequency > counter:
            counter = frequency
            frequent = i

    return frequent

user_1 = get_items()
user_2 = get_items()
user_3 = get_items()

final_list = merge_lists(user_1, user_2, user_3)

print("Najbardziej popularny przedmiot to:", most_popular(final_list))