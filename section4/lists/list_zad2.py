arr = []

for i in range(10):
    num = int(input("Podaj liczbe: "))
    arr.append(num)

for n in range(len(arr)):
    if arr[n] % 2 == 1:
        print(arr[n])