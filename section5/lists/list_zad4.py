arr = []

arr_lenght = int(input("Podaj parzysta dlugosc listy: "))

while arr_lenght % 2 == 1:
    print("Zle!")
    arr_lenght = int(input("Podaj parzysta dlugosc listy: "))

for i in range(arr_lenght):
    num = int(input("Podaj liczbe: "))
    arr.append(num)

mid = len(arr)//2
sec_mid = mid - 1

if arr[mid] == arr[sec_mid]:
    print("Dwie srodkowe liczby sa takie same")
else:
    print("Dwie srodkowe liczby nie sa takie same")