from random import randint


def read_quotes(file_name):
    with open(file_name + ".txt", 'r') as fopen:
        lines = fopen.readlines()
    
    return lines

def random_quote(quote_list):
    print("Quote of the day:\n")
    
    print("**************************************\n")
    print(quote_list[randint(0, 19)])
    print("**************************************")



def main():

    quotes = read_quotes(str(input("Podaj nazwe pliku: ")))

    random_quote(quotes)


if __name__ == "__main__":
    main()