import threading
import time


class Tasma(threading.Thread):
    def __init__(self, lock, name):
        threading.Thread.__init__(self)
        self.lock = lock
        self.name = name

    def run(self):
        a = 0
        for i in range(10):
            a += i
            print(a)
            time.sleep(1)
        self.lock.release()


lock = threading.Lock()
Tasma(lock, "thread1" + str(0)).start()
