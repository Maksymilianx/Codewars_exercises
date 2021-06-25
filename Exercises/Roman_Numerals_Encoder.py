anums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rnums = "M CM D CD C XC L XL X IX V IV I".split()

def solution(n):
    lst = []
    for a, r in zip(anums, rnums):
        x, n = divmod(n,a)
        lst.append(x * r)
    return ''.join(lst)


""" divmod(n,a) takes two numbers n,a, and returns a pair of numbers (quotient and remainder)
    in our case it begins from n / 1000 so quotient is 2 and remainder 21 """

