from _functools import reduce


def test(x, y):
    if isinstance(x, str) or isinstance(y, str):
        return int(x) * 10 + int(y)
    return x * 10 + y


l1 = [1, 2, 3, 4, 5]
l2 = ['1', '2', '3', '4']
print(reduce(test, l2))
