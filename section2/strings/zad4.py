# Zadanie 4
# Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
# Połącz dane w jeden ciąg book za pomocą spacji
# Policz liczbę wszystkich znaków w napisie book

title = str(input("Podaj tytul ksiazki: "))
author = str(input("Podaj nazwisko autora: "))
pages = int(input("Podaj liczbe stron: "))

book = title.title() + " " + author.title() + " " + str(pages)

print(book)
print("Liczba znakow:", len(book))