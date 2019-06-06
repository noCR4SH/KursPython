import bmi

def check_result(result):
    if result == "Niedowaga":
        with open('niedowaga.txt') as f:
            print(f.read())
    elif result == "Waga normalna":
        with open('normalna.txt') as f:
            print(f.read())
    elif result == "Nadwaga":
        with open('nadwaga.txt') as f:
            print(f.read())
    elif result == "Otylosc":
        with open('otylosc.txt') as f:
            print(f.read())

def main():
    mass = float(input('How much do you weight?: '))
    height = float(input('What is you height in meters?: '))

    result = bmi.calc(mass, height)

    check_result(result)
    

if __name__ == "__main__":
    main()