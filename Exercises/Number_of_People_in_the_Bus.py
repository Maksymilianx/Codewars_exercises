def numbers(bus_stops):
    nr_of_people = 0
    for nr in bus_stops:
        if nr[0]:
            nr_of_people += nr[0]
        if nr[1]:
            nr_of_people -= nr[1]
    return nr_of_people
