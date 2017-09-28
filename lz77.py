# coding=utf-8

if __name__ == '__main__':
    f = open('C:/Users/root/Desktop/te.jpg', 'rb')
    f1 = open('C:/Users/root/Desktop/test1.jpg', 'wb+')
    f.seek(0, 0)
    while True:
        byte = f.read()
        if byte != '':
            e = 0
            for i in byte:
                #a = ord(i)
                #b = e * 256 + a
                #print(b)
                f1.write(byte)
        else:
            break
    f1.close()
    f.close()
    print('finish')
