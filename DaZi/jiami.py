import base64

s = 'ojo'
a = base64.b64encode(s.encode("utf-8"))
z = base64.b64decode(a.decode('utf8'))
print(z)
