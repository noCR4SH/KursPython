arr = []

arr_lenght = int(input("Jak dluga ma byc lista?: "))

for i in range(arr_lenght):
    num = int(input("Podaj liczbe: "))
    arr.append(num)

if arr[0] == arr [-1]:
    print("Tak")
else:
    print("Nie")