def score(dice):
    """

    :param dice: a list of dice throws
    :return: a score for a dice throws
    """
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
    if 1 in dice:
        result += 100
    if 5 in dice:
        result += 50
    return result
