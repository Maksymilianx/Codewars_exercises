def permutations(string):
    result = {string}
    if len(string) == 2:
        result.add(string[1] + string[0])
    elif len(string) > 2:
        for i, c in enumerate(string):
            for x in permutations(string[:i] + string[i : 1:]):
                result.add(c + x)
    return list(result)
