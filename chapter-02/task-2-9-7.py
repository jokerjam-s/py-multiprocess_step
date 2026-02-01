from multiprocessing import Process


# Функция для суммирования элементов списка и вывода результата
def sum_list(numbers: list):
    print(f"Сумма элементов списка: {sum(numbers)}")


if __name__ == '__main__':
    list1 = [125, 2456, 3456, 4789]
    list2 = [5789, 646, 7756, 8746]

    # Создаем процессы для суммирования
    process1 = Process(target=sum_list, args=(list1,))
    process2 = Process(target=sum_list, args=(list2,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
