def find_short_words(fsw):
    lst = []
    for i in fsw:
        if len(i) < 5:
            lst.append(i)
    return lst
