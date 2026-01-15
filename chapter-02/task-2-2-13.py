import multiprocessing


def hello():
    print("Hello from a new process!")

if __name__ == '__main__':
    # Создайте процесс с использованием нужных параметров конструктора
    process = multiprocessing.Process(target=hello)

    # Запустите процесс
    process.start()

    # Ожидайте завершения процесса
    process.join()