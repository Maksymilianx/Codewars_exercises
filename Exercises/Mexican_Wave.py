def wave(people):
    """

    :param people: a word or words to be waved
    :return: a list of words with capital letter moving through
    """
    return [people[:i] + people[i].upper() + people[i + 1:] for i in range(len(people)) if people[i].isalpha()]

# isalpha() - check if all the characters in the text are letters and not: " ", $, %, #, etc.
