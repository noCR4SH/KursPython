# Zadanie 2
# Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy,
# utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = "test"
s2 = "Official"

s1_mid = len(s1)//2

s3 = s1[:s1_mid] + s2 + s1[s1_mid:]

print(s3)