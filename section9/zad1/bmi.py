def calc(m, h):
    verdict = ""
    bmi = m / h**2

    if bmi < 18.5:
        verdict = "Niedowaga"
    elif bmi > 30:
        verdict = "Otylosc"
    elif bmi > 25:
        verdict = "Nadwaga"
    else:
        verdict = "Waga normalna"
    
    return verdict