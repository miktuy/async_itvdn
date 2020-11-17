import os
import threading
from typing import Callable


def exec_watcher(func: Callable):
    threading.Timer(5.0, func).start()


def hello():
    for i in os.listdir('.'):
        print(i)
    exec_watcher(hello)

exec_watcher(hello)
