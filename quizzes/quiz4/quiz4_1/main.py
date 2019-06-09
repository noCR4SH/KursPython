import handling_errors as he


def main():
    people = int(input("How many people?: "))
    cookies = int(input("How many cookies?: "))

    cookies_per_person, cookies_left = he.party_planner(cookies, people)

    print("Cookies per person:", cookies_per_person)
    print("Cookies left:", cookies_left)


if __name__ == '__main__':
    main()