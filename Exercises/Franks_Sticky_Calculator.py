def sticky_calc(operation, val1, val2):
    stick = int(str(round(val1)) + str(round(val2)))
    if operation == '+':
        return round(stick + val2)
    elif operation == '-':
        return round(stick - val2)
    elif operation == '*':
        return round(stick * val2)
    elif operation == '/':
        return round(stick / val2)


def sticky_calc2(op, val1, val2):
    return eval(f"{round(val1)}{round(val2)} {op} {round(val2)}")
