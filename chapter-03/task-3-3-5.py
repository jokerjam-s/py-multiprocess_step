"""
Напишите код, где один процесс вычисляет значения квадратов чисел от 2 до 26 (не включительно)
с шагом 3 и передает эти результаты в виде словаря другому процессу, который и выводит полученный словарь в консоль.
"""
import multiprocessing


# Процесс-генератор словаря
def generate_squares(connection):
    data = {d: d**2 for d in range(2, 26, 3)}
    connection.send(data)


# Процесс-получатель словаря
def print_squares(connection):
    data = connection.recv()
    print(f"Получен словарь с квадратами чисел: {data}")

if __name__ == "__main__":
    conn1, conn2 = multiprocessing.Pipe(duplex=False)

    process1 = multiprocessing.Process(target=generate_squares, args=(conn2,))
    process2 = multiprocessing.Process(target=print_squares, args=(conn1,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()