def histogram(s):
    lst = []
    try:
        for i in s:
            for x in range(i):
                lst.append("#")
            lst.append("\n")
        x = "".join(lst)
        return x
    except:
        TypeError
