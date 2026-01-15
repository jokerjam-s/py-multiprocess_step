from multiprocessing import Process


# Функция для обработки элементов списка с использованием соответствующих коэффициентов

def process_list(data: list, *, coefficients: dict):
    '''
    data: список чисел.
    coefficients: словарь коэффициентов, где ключи соответствуют порядку элементов в списке data
    '''
    for item in zip(data, coefficients.values()):
        value = item[0]
        factor = item[1]
        result = factor * value
        print(f"Элемент {value} умножен на {factor}: результат = {result}")


if __name__ == '__main__':
    # Список чисел
    args = [2, 8, 9, 1, 10, 7, 5, 4, 2, 3]

    # Словарь коэффициентов
    kwargs = {'one': 3.6, 'two': 6.5, 'three': 9.0, 'four': 1.2, 'five': 1.5,
              'six': 8.5, 'seven': 2.1, 'eight': 4.2, 'nine': 7.8, 'ten': 3.0}

    # Создайте процесс, передаем список и словарь через args и kwargs
    process = Process(target=process_list, args=(args,), kwargs={"coefficients": kwargs})

    # Запустите процесс
    process.start()

    # Ожидайте завершения процесса
    process.join()
