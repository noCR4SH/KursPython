def bmi_calc(m, h):
    verdict = ""
    bmi = m / h**2

    if bmi < 18.5:
        verdict = "Niedowaga"
    elif bmi > 25:
        verdict = "Nadwaga"
    else:
        verdict = "Jest gitara"
    return verdict

mass = int(input('How much do you weight?: '))
height = float(input('What is you height in meters?: '))

bmi = bmi_calc(mass, height)

print(bmi)