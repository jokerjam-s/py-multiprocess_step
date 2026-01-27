import multiprocessing
import threading


# Функция, выполняемая в дочерних процессах
def task():
    process = multiprocessing.current_process()
    thread = threading.main_thread()
    print(f"Процесс: {process.name}, главный поток: {thread.name}")


if __name__ == '__main__':
    # Создайте 3 дочерних процесса
    processes = [multiprocessing.Process(target=task) for _ in range(3)]

    # Запустите процессы
    for p in processes:
        p.start()

    # Ждите завершения
    for p in processes:
        p.join()