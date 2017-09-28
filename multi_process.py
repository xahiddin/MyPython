import threading, time

balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10000):
        change_it(n)


if __name__ == "__main__":
    t = threading.Thread(target=run_thread, args=(5,))
    t = threading.Thread(target=run_thread, args=(8,))
    t.start()
    t.join()
    print(balance)
