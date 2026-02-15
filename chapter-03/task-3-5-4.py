import multiprocessing


# Процесс-генератор списка чисел
def generate_list(connection):
    lst = [84, 58, 19, 76, 8, 54, 50, 98, 85, 13]
    connection.send(lst)
    print(f"Список отправлен: {lst}")


# Процесс-вычислитель суммы
def calculate_sum(connection):
    lst = connection.recv()
    print(f"Получена сумма: {sum(lst)}")


if __name__ == "__main__":
    conn1, conn2 = multiprocessing.Pipe()

    # Запустите процессы
    process1 = multiprocessing.Process(target=generate_list, args=(conn1,))
    process2 = multiprocessing.Process(target=calculate_sum, args=(conn2,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
