import multiprocessing
import os


# Функция для печати PID текущего процесса и PID родительского процесса
def child_task():
    print(f"Дочерний процесс: PID = {os.getpid()}, PID родителя = {os.getppid()}")


if __name__ == '__main__':
    # Создайте и запустите дочерний процесс и дождитесь его
    process = multiprocessing.Process(target=child_task)

    process.start()
    process.join()
