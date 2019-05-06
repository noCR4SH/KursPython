mass = int(input('How much do you weight?: '))
height = float(input('What is you height in meters?: '))

bmi = mass / height**2


print(round(bmi, 2))