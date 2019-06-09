def party_planner(cookies, people):
    leftovers = None
    num_each = None

    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.

    try:
        num_each = cookies // people
        leftovers = cookies & people
    except ZeroDivisionError as e:
        print("Are you out of your mind?\nInvite someone!")


    return(num_each, leftovers)