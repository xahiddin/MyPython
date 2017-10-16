import threading, time

a = 0

def action(arg):
    global a
    a += arg
    time.sleep(1)

fir = time.time()
for i in range(101):
    t = threading.Thread(target=action, args=(i,))
    t.start()
sec = time.time()

print(sec - fir)
print('the arg is : %s ' % a)
