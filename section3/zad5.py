text = str(input("Wprowadz slowo: "))

text2 = text[::-1]

text.lower()
text2.lower()

if text == text2:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")