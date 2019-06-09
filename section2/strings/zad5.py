# Zadanie 5
# Palindrom to wyrażenie brzmiące tak samo czytane
# od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
# Pozwól użytkownikowi wprowadzić dowolne zdanie.
# Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

text = str(input("Wprowadz slowo: "))

text2 = text[::-1]

text.lower()
text2.lower()

if text == text2:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")