"""
Напишите код, который использует три дочерних процесса для распределения и обработки списка чисел.
Первый процесс разделяет числа на четные и нечетные, отправляет их в другие два процесса.
Один процесс суммирует четные числа, а другой — нечетные. Оба процесса передают результаты обратно в первый процесс,
который выводит суммы на экран.
"""
import multiprocessing


# Генерация списка из 55 элементов
def generate_list():
    return [x for x in range(2, 275, 5)]


# Процесс 1: Распределяет числа и печатает суммы
def distribute_numbers(connection_even, connection_odd, numbers):
    even_list = []
    odd_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    connection_even.send(even_list)
    connection_odd.send(odd_list)
    even_sum = connection_even.recv()
    odd_sum = connection_odd.recv()
    print(f"Процесс 1: Получено от Процесса 2 - сумма четных чисел = {even_sum}")
    print(f"Процесс 1: Получено от Процесса 3 - сумма нечетных чисел = {odd_sum}")


# Процесс 2: Суммирует четные числа
def sum_even_numbers(connection):
    lst_even = connection.recv()
    lst_sum = sum(lst_even)
    print(f"Процесс 2: Сумма четных чисел = {lst_sum}")
    connection.send(lst_sum)


# Процесс 3: Суммирует нечетные числа
def sum_odd_numbers(connection):
    lst_odd = connection.recv()
    lst_sum = sum(lst_odd)
    print(f"Процесс 3: Сумма нечетных чисел = {lst_sum}")
    connection.send(lst_sum)


if __name__ == "__main__":
    # Получение списка чисел
    lst = generate_list()

    # Создайте каналы связи для обмена данными:
    # Процесс1<->Процесс2 и Процесс1<->Процесс3
    con12, con21 = multiprocessing.Pipe()
    con13, con31 = multiprocessing.Pipe()

    # Создайте процессы
    process1 = multiprocessing.Process(target=distribute_numbers, args=(con12, con13, lst))
    process2 = multiprocessing.Process(target=sum_even_numbers, args=(con21,))
    process3 = multiprocessing.Process(target=sum_odd_numbers, args=(con31,))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()
