from multiprocessing import Process


# Допишите функцию, которую будет выполнять процесс
def sum_numbers(numbers):
    total = sum(numbers)
    print(f"Сумма чисел: {total}")


if __name__ == '__main__':
    # Список чисел для суммирования
    numbers = [5, 10, 15, 20, 25]

    # Создаем процесс с использованием нужных параметров конструктора
    process = Process(target=sum_numbers, args=(numbers,))

    # Запускаем процесс
    process.start()

    # Ожидаем завершения процесса
    process.join()
