data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

def print_calendar(data):
    start_day = 0
    for month, days in data:
        print('\n')
        print(month)
        print('{0:<4}'.format('')*start_day, end = '')
        start_day = print_week(days, start_day)

def print_week(days, start_day):
    for day in days:
        print('{0:<4}'.format(day), end = '')
        start_day += 1
        start_day = sunday_reset(start_day) if start_day == 7 else start_day
    return start_day

def sunday_reset(start_day):
    print()
    start_day = 0
    return start_day

print_calendar(data)