from multiprocessing import Process
from time import sleep


# Функция для выполнения процесса с задержкой
def task(delay):
    sleep(delay)


if __name__ == '__main__':
    # Словарь с именами процессов и задержкой
    processes_data = {
        'process_1': 4,
        'process_2': 5,
        'process_3': 2
    }

    # Создайте и запустите процессы
    processes = [Process(target=task, name=n, args=(d,)) for n, d in processes_data.items()]

    for process in processes:
        process.start()

    sleep(3)
    for process in processes:
        if process.is_alive():
            print(f"Процесс {process.name}: активен")
            process.join()
        else:
            print(f"Процесс {process.name}: завершен")

    for process in processes:
        print(f"Процесс {process.name} завершился с кодом {process.exitcode}")
