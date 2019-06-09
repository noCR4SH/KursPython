def list_sum():
    nums = []
    sum = 0
    list_size = int(input("Jak duza ma byc lista: "))

    for i in range(list_size):
        num = int(input("Podaj numer: "))
        nums.append(num)
    
    for i in nums:
        sum += i

    return sum

result = list_sum()

print("Suma wynosi:", result)
