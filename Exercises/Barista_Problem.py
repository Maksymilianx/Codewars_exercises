def barista(coffees):
    sorted_coffees = sorted(coffees)
    previous_coffee = sorted_coffees[0]
    total = 0
    for x in sorted_coffees[1:]:
        total += previous_coffee
        previous_coffee = previous_coffee + 2 + x
    return total + previous_coffee


print(barista([1,2,3]))