import functools
from typing import Coroutine, Callable


def is_divider(number):
    print('Coroutine started')
    while True:
        value = yield
        if number % value == 0:
            print(value)


cor = is_divider(100)
cor.send(None)
cor.send(18)
cor.send(20)
cor.close()


def coroutine(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Coroutine:
        res = func(*args, **kwargs)
        res.send(None)
        return res
    return wrapper


@coroutine
def is_divider(number):
    print('Coroutine started')
    while True:
        value = yield
        if number % value == 0:
            print(value)


cor = is_divider(100)
cor.send(11)
cor.send(18)
cor.send(20)
cor.close()