"""
Распределение данных между процессами с использованием очереди
"""
import multiprocessing
import queue
from time import sleep


def worker(queue_in, queue_out):
    while not queue_in.empty():
        sleep(0.1)
        try:
            number = queue_in.get(block=False)
            queue_out.put(number * number)
        except queue.Empty:
            pass


if __name__ == '__main__':
    numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    task_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()

    for number in numbers:
        task_queue.put(number)

    # Создайте и запустите 3 рабочих процесса
    processes = [multiprocessing.Process(target=worker, args=(task_queue, result_queue)) for _ in range(4)]
    for process in processes:
        process.start()

    for process in processes:
        process.join()

    result = []
    while not result_queue.empty():
        result.append(result_queue.get())

    print(result)