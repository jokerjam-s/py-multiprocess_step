from multiprocessing import Process
from time import sleep


# Функции one_task(), two_task() и three_task() уже определены под капотом.

def one_task():
    sleep(1)


def two_task():
    sleep(1)


def three_task():
    try:
        sleep(1)
        raise ValueError("Ошибка в процессе")
    except ValueError as e:
        # Обрабатываем ошибку и вручную задаем exitcode как 1
        exit(1)


if __name__ == '__main__':
    processes = [
        Process(target=one_task, name="one_task"),
        Process(target=two_task, name="two_task"),
        Process(target=three_task, name="three_task"),
    ]

    for process in processes:
        process.start()
    for process in processes:
        process.join()

    for process in processes:
        if process.exitcode == 0:
            print(f'Процесс {process.name} завершился успешно с кодом {process.exitcode}')
        else:
            print(f'Процесс {process.name} завершился с ошибкой с кодом {process.exitcode}')
