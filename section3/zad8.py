# Zadanie 8
# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

txt = str(input("Wprowadz wyraz: "))

print(txt[1::2])

for i in range(1, len(txt), 2):
    print(txt[i])