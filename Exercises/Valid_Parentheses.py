def valid_parentheses(string):
    lst = []
    for i in string:
        if i == '(':
            lst.append(i)
        elif i == ')':
            try:
                lst.pop()
            except:
                return False
    if len(lst) == 0:
        return True
    else:
        return False


""" for every '(' in string for loop will add '(' to list[] and for every ')' loop will try to remove each ')'. 
    If in argument string will be to many ')' exception will occurs as False because there is nothing to .pop() from the 
    list, in result if list will be empty function will return True, if not False"""
