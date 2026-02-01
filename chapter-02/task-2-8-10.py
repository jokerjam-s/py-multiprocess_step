from multiprocessing import Process
from time import sleep


# Функция для выполнения процесса с заданной задержкой
def task(delay):
    sleep(delay)


if __name__ == '__main__':
    # Словарь с именами процессов и временем задержки
    processes_data = {
        'process_1': 2,
        'process_2': 5,
        'process_3': 4,
        'process_4': 7,
        'process_5': 8
    }

    # Создание процессов
    processes = [Process(target=task, name=n, args=(d,)) for n, d in processes_data.items()]

    for process in processes:
        process.start()

    for _ in range(0, 3):
        print("Текущий статус процессов:")
        for process in processes:
            print(f"Процесс {process.name}: {'активен' if process.is_alive() else 'завершен'}")
        sleep(3)
