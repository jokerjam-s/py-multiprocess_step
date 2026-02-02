import multiprocessing
import ctypes
from multiprocessing import Process


# Функции для каждого процесса, выполняющие соответствующую операцию
def multiply_by_2(numbers, results1):
    for n, r in zip(numbers, results1):
        r.value = n * 2.5
    print(f"Процесс умножения на 2.5: {[r.value for r in results1]}")


def square(numbers, results2):
    for n, r in zip(numbers, results2):
        r.value = n**2.5
    print(f"Процесс возведения в степень 2.5: {[round(r.value, 1) for r in results2]}")


if __name__ == '__main__':
    numbers = [11, 21, 31, 41, 51]

    # Создайте списки multiprocessing.Value для хранения результатов работы для каждого процесса
    results1 = [multiprocessing.Value(ctypes.c_double) for _ in range(0, len(numbers))]
    results2 = [multiprocessing.Value(ctypes.c_double) for _ in range(0, len(numbers))]

    # Создание процессов для каждой операции
    process1 = Process(target=multiply_by_2, args=(numbers, results1))
    process2 = Process(target=square, args=(numbers, results2))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    final_results1 = [v.value for v in results1]
    final_results2 = [round(v.value, 1) for v in results2]

    print(f'Результаты умножения на 2.5: {sum(final_results1)}')
    print(f'Результаты возведения в степень 2.5: {sum(final_results2)}')
