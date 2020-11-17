from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor
from functools import reduce
from operator import add
import time


def handler(started: int = 0, finished: int = 0) -> int:
    return reduce(add, range(started, finished))


def run_by_executor(executor_class: Executor, max_workers: int = 4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()
    future1 = executor.submit(handler, started=0, finished=2 ** 26)
    future2 = executor.submit(handler, started=2 ** 26, finished=2 ** 28)

    result = future2.result() + future1.result()
    spent_time = time.time() - started
    print(f'Result: {result}. Time for {executor_class.__name__}: {spent_time}')


def run_by_executor_map(executor_class: Executor, max_workers: int = 4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()
    params = [
        [0, 2 ** 26],
        [2 ** 26, 2 ** 28]
    ]
    result = sum(executor.map(handler, *params))
    spent_time = time.time() - started
    print(f'Result: {result}. Time for {executor_class.__name__}: {spent_time}')


if __name__ == '__main__':
    print('Execute using map...')
    run_by_executor_map(ThreadPoolExecutor)
    run_by_executor_map(ProcessPoolExecutor)

    print('Execute using submit...')
    run_by_executor(ThreadPoolExecutor)
    run_by_executor(ProcessPoolExecutor)