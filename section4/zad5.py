# Zadanie 5
# Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for.

start = 0
limit = 200
step = 20

fahr = start

print("Wykonane petla while: ")
while(fahr <= limit):
    celsius = 5 / 9 * (fahr - 32)
    print(fahr, "\t", celsius)
    fahr = fahr + step

print("\n")

print("Wykonane petla for:")
for i in range(start, 201, step):
    celsius = 5 / 9 * (i - 32)
    fahr = i
    print(fahr, "\t", celsius)
    