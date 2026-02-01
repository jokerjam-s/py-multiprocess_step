from multiprocessing import Process
from time import sleep


# Функция для запуска в процессе
def task(name, delay):
    """Задача отрабатывает задержку и печатает сообщение о завершении процесса"""
    sleep(delay)
    print(f"Процесс {name} завершен с задержкой: {delay} секунд")


if __name__ == '__main__':
    delays = [2.4, 3.2, 3.0, 2.0, 8.7, 3.3, 7.2, 7.0, 6.4, 7.5]  # Задержки для задач
    names = [
        'Исследователь',
        'Путешественник',
        'Маг',
        'Альпинист',
        'Астроном',
        'Воин',
        'Загадочник',
        'Завоеватель',
        'Садовод',
        'Проводник'
    ]

    processes = []
    for n, d in zip(names, delays):
        p = Process(target=task, name=n, args=(n, d,))
        processes.append(p)
        p.start()

    processes[0].join(timeout=2.5)

    for p in processes:
        if p.exitcode is None:
            print(f"Процесс {p.name} еще выполняется")

    processes[4].join()