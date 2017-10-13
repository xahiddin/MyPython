import queue
from threading import Thread
import os
import urllib.request
import urllib.error

target = "http://anewme.cn"
directory = '../'
filters = [".jpg", ".png", ".gif", ".css", ".jpeg"]

os.chdir(directory)


w_path = queue.Queue()

for r, d, f in os.walk("."):
    for files in f:
        r_path = "%s/%s" % (r, files)
        if r_path.startswith("."):
            r_path = r_path[1:]
        if os.path.splitext(files)[1] not in filters:
            w_path.put(r_path)


def test_remote():
    while not w_path.empty():
        path = w_path.get()
        url = "%s/%s" % (target, path)

        try:
            response = urllib.request.urlopen(url)
            content = response.read()
            print("[%d]==>%s" % (response.code, path))
            response.close()

        except urllib.error.HTTPError as reason:
            print(reason.code)


for i in range(0, 10):
    t = Thread(target=test_remote())
    t.start()
