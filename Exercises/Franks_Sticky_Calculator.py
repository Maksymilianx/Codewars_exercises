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
