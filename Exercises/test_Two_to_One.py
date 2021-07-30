from Exercises.Two_to_One import longest


def test_longest():
    x = 'kupa'
    y = 'kaszalot'
    assert longest(x, y) == "aklopstuz"


def test_longest2():
    x = 'color'
    y = 'cringe'
    assert longest(x, y) == "cegilnor"
