import multiprocessing
import time


# Функция, выполняемая дочерними процессами (пустая функция)
def task():
    time.sleep(0.2)


if __name__ == '__main__':
    # Создайте 5 дочерних процессов
    children = [multiprocessing.Process(target=task) for _ in range(5)]

    # Запустите дочерние процессы
    for child in children:
        child.start()


    # Получите список активных дочерних процессов
    processes = multiprocessing.active_children()
    for p in processes:
        print(p)

    # Ожидайте завершения всех дочерних процессов
    for p in processes:
        p.join()