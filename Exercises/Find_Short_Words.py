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

def FindShortWords(x):
    return [ x for x in x if len(x) < 5 ]

print(FindShortWords(['asddfff', 'asd', 'gfagaga']))