import zipfile
from threading import Thread

path = r'E:\test.zip'


def test(zFile, passwd):
    try:
        zFile.extractall(pwd=passwd)
        print(passwd.decode("utf8"))
    except:
        return


def broke(path):
    zFile = zipfile.ZipFile(path)
    with open('dict.txt')as f:
        for line in f.readlines():
            passwd = line.strip("\r\n").encode("utf-8")
            t = Thread(target=test, args=(zFile, passwd))
            t.start()


if __name__ == '__main__':
    broke(path)
