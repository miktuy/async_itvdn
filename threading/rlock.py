# DEADLOCK escaping
import threading

def producer():
    print('Set locking')
    with lock:
        print('done')
        with lock:
            print("It's great")
    print('Locking release!')

lock = threading.RLock()
# __enter__ => lock.acquire()
# __exit__ => lock.release()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()