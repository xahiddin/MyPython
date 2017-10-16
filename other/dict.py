from time import time
fo = open("E:\\6n1alpha.txt", "w")
zimu = [chr(x) for x in range(97, 123)]
print(time())
for i in range(0, 1000000):
    for a in zimu:
        if i < 10:
            fo.write("00000%s%s\n" % (i, a))
        if 100 > i > 10:
            fo.write("0000%s%s\n" % (i, a))
        if 1000 > i > 100:
            fo.write("000%s%s\n" % (i, a))
        if 10000 > i > 1000:
            fo.write("00%s%s\n" % (i, a))
        if 100000 > i > 10000:
            fo.write("0%s%s\n" % (i, a))
        if i > 100000:
            fo.write("%s%s\n" % (i, a))

fo.close()
print(time())