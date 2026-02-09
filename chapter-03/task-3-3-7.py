import multiprocessing
from multiprocessing import Process, Array
import ctypes


def square_number(shared_array, i):
    shared_array[i] = shared_array[i] ** 2


if __name__ == '__main__':
    numbers = [33, 55, 11, 44, 99]
    shared_array = multiprocessing.Array(ctypes.c_int, numbers)

    processes = [Process(target=square_number, args=(shared_array, i)) for i in range(len(numbers))]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print( f"Квадраты чисел: {shared_array[:]}")
