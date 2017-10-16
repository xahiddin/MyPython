def find(demo):
    c = 0
    if not isinstance(demo, list):
        return c
    else:
        c += 1
        deeps = []
        for i in demo:
            deeps.append(find(i))
        deeps.sort()
        c += deeps[-1]
        return c


demo = [[1], [[2], [3, 2, [3, [33]]]], [[[3]]]]
print(find(demo))
