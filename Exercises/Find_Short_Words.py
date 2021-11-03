def find_short_words(fsw):
    """

    :param fsw: a list of strings
    :return: a list of words smaller than 5
    """
    lst = []
    for i in fsw:
        if len(i) < 5:
            lst.append(i)
    return lst


def FindShortWords(fsw):
    return [x for x in fsw if len(x) < 5]


print(FindShortWords(['asddfff', 'asd', 'gfagaga']))
