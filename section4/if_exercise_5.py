password = str(input("Podaj haslo: "))

if len(password) < 8:
    print("Haslo za krotkie")
elif password.islower() == True:
    print("Brak duzej")
elif password.isupper() == True:
    print("Za duzo tych duzych")
elif password.isalpha() == True:
    print("Brak cyfry")
elif password.isdecimal() == True:
    print("Wez dodaj jakies litery")
elif password.isalnum() == False:
    print("Czy ty jestes jakis specjalny?")
else:
    print("Gitara siema")