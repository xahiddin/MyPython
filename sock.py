import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.20.", 8888))

s.send('test')

buf = []

while True:
    d = s.recv(1024)
    if d:
        buf.append(d)
    else:
        break

print("".join(buf))
