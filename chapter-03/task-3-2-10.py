# Импортируйте необходимые модули
import ctypes
import math
from multiprocessing import Value, Process

# Функция для вычисления факториала числа
def new_calculate_factorial(n, result):
    value = math.factorial(n)
    result.value += value
    print(f"Факториал {n} = {value}")

if __name__ == '__main__':
    numbers = [3, 5, 9, 11, 13]
    # Создайте объект multiprocessing.Value
    result = Value(ctypes.c_int64, 0)

    # Создайте процессы и запустите их
    processes = [Process(target=new_calculate_factorial, args=(n, result)) for n in numbers]
    for p in processes:
        p.start()

    # Дождитесь завершения работы дочерних потоков и выведите результат
    for p in processes:
        p.join()

    print(f'Сумма факториалов чисел из списка {numbers}: {result.value}')