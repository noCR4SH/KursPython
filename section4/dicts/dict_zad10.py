result = {}

n = int(input("Podaj liczbe N: "))

for i in range(n):
    num = i + 1
    result[str(num)] =  num * num

for key, value in result.items():
    print(key, ":", value)