def is_visa(number):
    if len_of_number not in [13, 16]:
        return False
    else:
        if number[0] == "4":
            return True
        else:
            return False

def is_mastercard(number):
    if len_of_number != 16:
        return False
    else:
        if int(number[:2]) >= 51 and int(number[:2]) <= 55:
            return True
        elif int(number[:4]) >= 2221 and int(number[:4]) <= 2720:
            return True
        else:
            return False

def is_american_expert(number):
    if len_of_number != 15:
        return False
    else:
        if number[:2] == "34" or number[:2] == "37"
            return True
        else:
            return False

number = input("Podaj numer karty: ")

#czy numer jest bledny
len_of_number = len(number)

if len_of_number not in [13, 15, 16]:
    print("Gdzie mnie z tym numerem!")


#czy visa
if is_visa(number):
    print("Buzie VISE")
#czy master
elif is_mastercard(number):
    print("to mastercad, maj master")
#czy american
elif is_american_expert(number):
    print("America! Fuck Yeah!")