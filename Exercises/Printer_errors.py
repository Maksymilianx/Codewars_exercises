def printer_error(s):
    allowed = "abcdefghijklm"
    errors = 0
    for letter in s:
        if letter not in allowed:
            errors += 1
    return f"{errors}/{len(s)}"


def another_approach(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
