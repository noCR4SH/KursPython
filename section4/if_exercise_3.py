rate1 = int(input("Ocena okladke: "))
rate2 = int(input("Ocena fabuly: "))
rate3 = int(input("Ocena dlugosci: "))

mean = (rate1 + rate2 + rate3) / 3

if mean >= 7:
    print("Ksiazka bardzo fajna: ", mean, "/ 10")
elif mean > 5:
    print("Ksiazka jest OK: ", mean, "/ 10")
else:
    print("No slabo troche: ", mean, "/ 10")