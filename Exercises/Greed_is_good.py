def score(dice):
    """

    :param dice: a list of dice throws
    :return: a score for a dice throws
    """
    if type(dice) not in [list]:
        raise TypeError("The given parameter should be a list")
    result = 0
    for i in range(1,7):
        if dice.count(i) > 2:
            # .count() count how many i is in the list
            if i == 1:
                result = 1000
            else:
                result = i * 100
            for x in range(3):
                del dice[dice.index(i)]
            break
    if dice.count(1) == 1:
        result += 100
    elif dice.count(1) == 2:
        result += 200
    if dice.count(5) == 1:
        result += 50
    elif dice.count(5) == 2:
        result += 100
    return result

print(score([1,1,1,1,1]))