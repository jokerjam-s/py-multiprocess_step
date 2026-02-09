from multiprocessing import Process, Array
import ctypes


# Функция для изменения элемента массива
def modify_element(shared_array, i):
    if shared_array[i] % 2 == 0:
        shared_array[i] = shared_array[i] * i
    else:
        shared_array[i] = shared_array[i] - i


if __name__ == '__main__':
    # Исходные данные
    initial_data = [13, 5, 8, 6, 10, 7, 14, 21, 9, 4]

    # Создайте общий массив
    shared_array = Array(ctypes.c_int, initial_data)

    # Создайте процессы для изменения элементов массива
    processes = [Process(target=modify_element, args=(shared_array, i)) for i in range(len(initial_data))]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"Измененный массив: {shared_array[:]}")
