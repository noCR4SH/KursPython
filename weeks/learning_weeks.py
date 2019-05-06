import constants

hours_per_week = int(input('How many hours are you learning per week?: '))

weeks_to_learn = constants.HOURS / hours_per_week


if weeks_to_learn > 1:
    print("It will take you", round(weeks_to_learn), "weeks to learn new skill.")
else:
    print("It will take you", round(weeks_to_learn), "week to learn new skill.")