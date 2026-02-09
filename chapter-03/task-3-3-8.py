from multiprocessing import Process, Array
import ctypes


# Функция для увеличения значения по индексу на значение индекса
def increment(shared_array, index):
    shared_array[index] += index


if __name__ == '__main__':
    # Создайте общий массив из 5 элементов, инициализированных нулями, с применением Array
    shared_array = Array(ctypes.c_int, 5)

    # Создайте 5 процессов, каждый из которых увеличивает элемент массива на его индекс в функции increment()
    processes = [Process(target=increment, args=(shared_array, i)) for i in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f"Итоговый массив: {shared_array[:]}")
