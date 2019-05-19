i = 0

subject = []
grade = []

while (i < 4):
    subject.append(str(input("Podaj nazwe przedmiotu: ")))
    grade.append(int(input("Podaj ocene od 1-6: ")))
    i += 1

for n in subject:
    print(subject[n])

    #do dokonczenia
    