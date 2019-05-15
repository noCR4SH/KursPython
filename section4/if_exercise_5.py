password = str(input("Podaj haslo: "))

if len(password) < 8:
    print("Haslo za krotkie")
elif password.islower() == True:
    print("Brak duzej")
elif password.isalpha() == True:
    print("Brak cyfry")
elif password.isdecimal() == True:
    print("Wez dodaj jakies litery")
else:
    print("Gitara siema")