import threading
import time

def print_epoch(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "-----------", time.time(), "\n")

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    # Overriding the run method from threading
    def run(self):
        print("start thread:", self.name)
        print_epoch(self.name, self.delay)
        print("end thread:", self.name)

if __name__ == "__main__":
    t1 = MyThread("Thread-1",1)
    t2 = MyThread("Thread-2",2)

    t1.start()
    t2.start()

    print(t1.getName())
    print(t2.getName())
    print(threading.active_count())
    print(threading.currentThread())
    print(threading.enumerate())

    t1.join()
    t2.join()