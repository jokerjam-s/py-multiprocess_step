import os
from multiprocessing import Process
from time import sleep


# Реализуйте во всех функциях task() корректный вывод PID, и запустите их в разных процессах
def task_1():
    sleep(1)
    print(f"Процесс 1 завершен: PID = {os.getpid()}")


def task_2():
    sleep(2)
    print(f"Процесс 2 завершен: PID = {os.getpid()}")


def task_3():
    sleep(3)
    print(f"Процесс 3 завершен: PID = {os.getpid()}")


if __name__ == '__main__':
    # Создайте три дочерних процесса и дождитесь их завершения
    processes = [Process(target=task_1), Process(target=task_2), Process(target=task_3)]

    for process in processes:
        process.start()
    for process in processes:
        process.join()
