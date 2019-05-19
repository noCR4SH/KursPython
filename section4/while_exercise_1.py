start = 0
limit = 200
step = 20

fahr = start

while(fahr <= limit):
    celsius = 5 / 9 * (fahr - 32)
    print(fahr, "\t", celsius)
    fahr = fahr + step