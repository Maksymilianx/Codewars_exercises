def sum_pairs(ints, s):
    """

    :param ints: any integers
    :param s: number to find
    :return: two integers that in a sum gives param s
    """
    cache = set()
    # set() method is used to convert any of the iterable to sequence of iterable elements.
    # Returns empty if no elements is passed.
    for i in ints:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

# print(sum_pairs([1,2,3,4,5,6], 6))

