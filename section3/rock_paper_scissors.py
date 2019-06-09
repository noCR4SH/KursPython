# Zadanie 10
# Napisz grę - kamień (k) / papier (p) / nożyce (n).
# Użytkownik podaje jedną z 3 figur.
# Komputer losuje jedną z 3 figur.
# Sprawdź kto wygrał tę rundę.
#
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random

txt_options = "Kamien =  0\nPapier = 1\nNozyce = 2\nKoniec gry = 5\n\n"
txt_win = "Wygrales!"
txt_lose = "Przegrales!"
txt_draw = "Remis!"
txt_start = "Jaki jest twoj wybor: "

options_list = ["Kamien", "Papier", "Nozyce"]
player_points = 0
computer_points = 0
current_round = 0

rounds = int(input("Podaj liczbe rund: "))

while current_round != rounds:
    computer_choice = random.randint(0, 2)

    print("--------------------------")
    player_choice = int(input(txt_options + txt_start))
    print("\n")

    if computer_choice == player_choice:
        print(txt_draw)

        current_round += 1

    elif player_choice == 0:

        if computer_choice == 1:
            print(txt_lose, options_list[1], "pokrywa", options_list[0])
            
            computer_points += 1
            current_round += 1
        else:
            print(txt_win, options_list[0], "rozwala", options_list[2])
            player_points += 1
            current_round +=1

    elif player_choice == 1:

        if computer_choice == 2:
            print(txt_lose, options_list[2], "przecina", options_list[1])
            
            computer_points += 1
            current_round += 1
        else:
            print(txt_win, options_list[1], "pokrywa", options_list[0])
            player_points += 1
            current_round +=1

    elif player_choice == 2:

        if computer_choice == 1:
            print(txt_lose, options_list[0], "pokrywa", options_list[2])
            
            computer_points += 1
            current_round += 1
        else:
            print(txt_win, options_list[2], "przecina", options_list[1])
            player_points += 1
            current_round +=1
    elif player_choice == 5:
        print("Wyszedles z gry.")
        current_round = rounds

if player_points > computer_points:
    print(txt_win, player_points, ":", computer_points)
elif player_points == computer_points:
    print(txt_draw, player_points, ":", computer_points)
else:
    print(txt_lose, player_points, ":", computer_points)
        

