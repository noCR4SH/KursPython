shelf = {}

def get_details():
    shelf_size = int(input("Ile chcesz podac ksiazek: "))

    for i in range(shelf_size):
        book_name = str(input("Podaj nazwe ksiazki: "))
        book_rate = str(input("Podaj ocene ksiazki: "))
        shelf[book_name] = book_rate
        

    return shelf

def shelf_output(book):
    print("Ocena wybranej ksiazki", book, "to:", shelf[book])

list_of_books = get_details()
print(list_of_books)

name_of_book = str(input("Podaj nazwe: "))

if name_of_book in shelf:
    shelf_output(name_of_book)
else:
    print("Ni ma")

