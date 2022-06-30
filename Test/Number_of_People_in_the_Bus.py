from Exercises.Number_of_People_in_the_Bus import numbers

def test_number_of_people():
    people = [[10,0],[3,5],[5,8]]
    remaining_people = 5
    assert numbers(people) == remaining_people

def test_number_of_people2():
    people = [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]
    remainig_people = 17
    assert numbers(people) == remainig_people

def test_number_of_people3():
    people = [[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]
    remaining_people = 21
    assert numbers(people) == remaining_people
