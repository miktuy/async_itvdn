import logging
import threading
import time


file_handler = logging.FileHandler("debug.log")
logger = logging.getLogger("app_logger")
logger.setLevel("DEBUG")
std_format = logging.Formatter(fmt="{asctime} - {levelname} - {name} - {message}", style="{")
logger.addHandler(file_handler)
file_handler.setFormatter(std_format)


def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += i
    print(f'Value: {result}')


params = {'finished': 2 ** 26}

task = threading.Thread(target=handler, kwargs=params)
started_at = time.time()
logger.debug('RESULT 1')
task.start()
task.join()
logger.debug(f'Time: {time.time() - started_at}')

started_at = time.time()
logger.debug('RESULTS 2')
handler(**params)
logger.debug(f'Time: {time.time() - started_at}')