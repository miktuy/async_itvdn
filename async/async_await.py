import asyncio


async def worker(number, divider):
    print(f'Worker {number} started')
    await asyncio.sleep(1)
    print(number / divider)
    return number / divider


async def gather_worker():
    result = await asyncio.gather(
        worker(50, 10),
        worker(60, 10),
        worker(70, 10),
        worker(80, 10),
        worker(90, 10),
    )
    print(result)


event_loop = asyncio.get_event_loop()
task_list = [
    worker(30, 10),
    asyncio.ensure_future(worker(30, 10)),
    event_loop.create_task(gather_worker())
]

tasks = asyncio.wait(task_list)
event_loop.run_until_complete(tasks)
event_loop.close()