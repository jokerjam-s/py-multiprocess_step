import multiprocessing
from multiprocessing import Process, current_process


# Функция, выполняемая в дочернем процессе
def task():
    this_process = current_process()
    parent_process = multiprocessing.parent_process()

    if parent_process:
        print(f"Родительский процесс: {parent_process.name}")

    print(f"Дочерний процесс: {this_process.name}")


if __name__ == '__main__':
    # Создайте дочерний процесс и назначьте имя дочернему процессу
    process = Process(target=task, name="ChildProcess_1")

    # Запустите дочерний процесс
    process.start()

    # Ожидайте завершения дочернего процесса
    process.join()