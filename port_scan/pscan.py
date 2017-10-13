import socket, time
import threading


# 123.57.220.107

def pscan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((ip, port))
        time.sleep(0.5)
        if res == 0:
            print("port {} is opened".format(port))
        sock.close()
    except socket.error:
        print("can't connect")


def th(from_, to_):
    ip = input("ip>>")
    try:
        for i in range(from_, to_):
            t = threading.Thread(target=pscan, args=(ip, i))
            time.sleep(0.001)
            t.start()
    except Exception:
        pass


th(1, 1000)
