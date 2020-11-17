import threading
import time

def producer():
    with lock:
        print('Set locking', lock._value)
        time.sleep(3)
        print("I'm free")


MAX_WORKERS = 1
lock = threading.BoundedSemaphore(value=MAX_WORKERS)

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)
task3 = threading.Thread(target=producer)
task4 = threading.Thread(target=producer)

task1.start()
task2.start()
task3.start()
task4.start()

task1.join()
task2.join()
task3.join()
task4.join()

lock.release()