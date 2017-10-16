a = [9, 8, 7, 6, 5, 4, 3, 2, 1]

ll = 0
for j in range(len(a) - 1):
    for i in range(len(a) - 1):
        if (a[i] > a[i + 1]):
            ll = a[i]
            a[i] = a[i + 1]
            a[i + 1] = ll
        print(a)

