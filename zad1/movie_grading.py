movie = input('Movie title: ')
costume_grade = int(input('Costume grade: '))
story_grade = int(input('Story grade: '))
visuals_grade = int(input('Visuals grade: '))
characters_grade = int(input('Characters grade: '))

overall_grade = (costume_grade + story_grade + visuals_grade + characters_grade) / 4

print()
print("Movie: " + movie)
print("Overall grade: ", overall_grade)

