from multiprocessing import Process


# Функция для суммирования чисел
def sum_numbers(numbers):
    total = sum(numbers)
    print(f"Сумма чисел: {total}")


# Функция для вычисления среднего значения
def average_numbers(numbers):
    avg = sum(numbers) / len(numbers)
    print(f"Среднее значение чисел: {avg}")


if __name__ == '__main__':
    # Список для суммирования
    sum_list = [50, 100, 105, 200, 250]

    # Список для вычисления среднего значения
    avg_list = [20, 40, 60, 80, 100]

    # Создаем два процесса с различными целями
    sum_process = Process(target=sum_numbers, args=(sum_list,))
    avg_process = Process(target=average_numbers, args=(avg_list,))

    # Запустите процессы
    sum_process.start()
    avg_process.start()

    # Ожидайте завершения обоих процессов
    sum_process.join()
    avg_process.join()
