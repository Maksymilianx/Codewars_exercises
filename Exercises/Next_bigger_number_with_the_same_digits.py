def next_bigger(n):
    """

    :param n: an integer
    :return: a next bigger integer
    """
    arr = list(str(n))
    # max_n reverse and sort the list to get the largest number
    max_n = int("".join(sorted(arr, reverse=True)))
    # min_n sort a list to get the min. number
    min_n = sorted(arr)
    m = n
    while m <= max_n:
        m += 1
        # if number is found in our min_n list then return the new number
        if sorted(list(str(m))) == min_n:
            return m
    return -1
