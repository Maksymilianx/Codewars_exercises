def move_zeros(array):
    """

    :param array: takes a list of integers
    :return: a list of integers with every 0 moved to the end of list
    """
    result = []
    rest = []
    for x in array:
        if x != 0:
            result.append(x)
        else:
            rest.append(x)
    result.extend(rest)
    return result
