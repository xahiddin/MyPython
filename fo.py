if __name__ == '__main__':
    f = open("C:/Users/root/Desktop/reverseMe", 'rb+')
    f_new = open("C:/Users/root/Desktop/reverseMe.jpeg", 'wb+')
    f.seek(0, 0)
    byte = f.read()
    #f_new.write(byte)
    f_new.write(byte[::-1])#tetur yizish
    f.close()
    f_new.close()
