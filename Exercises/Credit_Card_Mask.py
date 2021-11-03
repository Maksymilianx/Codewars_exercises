def maskify(cc):
    word = list(cc)
    for i in range(len(word) - 4):
        word[i] = '#'
    return "".join(word)

print(maskify("1824852943218931"))