# Zadanie 1
# Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7
# i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

word = "Astronomy"

sr_index = len(word)//2

sr_word = word[sr_index-1] + word[sr_index] + word[sr_index+1]

print(sr_word)