# Импортируйте необходимые модули
from multiprocessing import Process, Value


# Функция для вычисления факториала числа
def calculate_factorial(n: int, result: Value):
    for i in range(n, 0, -1):
        result.value *= i


if __name__ == '__main__':
    numbers = [2, 4, 6, 8, 10]
    # Создайте список multiprocessing.Value для хранения результатов работы для каждого процесса
    results = [Value('i', 1) for _ in range(0, len(numbers))]

    processes = [
        Process(target=calculate_factorial, args=(value, results[index]))
        for index, value in enumerate(numbers)
    ]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    for index, value in enumerate(results):
        print(f'Факториал {numbers[index]} = {results[index].value}')
