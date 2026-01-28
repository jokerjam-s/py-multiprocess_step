# Переменная target_names и её содержимое скрыто под капотом, она содержит список из трех имен процессов, которые необходимо убить с помощью kill()
from black.nodes import child_towards

target_names = ["Тюлень", "Черепаха", "Ёжик"]

import time
import multiprocessing


# Функция поиска и завершения процессов по их именам
def kill_processes_by_names(target_names):
    child_process = multiprocessing.active_children()
    for process in child_process:
        if process.name in target_names:
            print(f"Процесс {process.name} найден и будет завершен.")
            process.kill()
            print(f"Процесс {process.name} завершен.")
        else:
            print(f"Процесс {process.name} отработал до конца.")

# Задача, выполняемая процессом
def task():
    time.sleep(3)  # процесс будет "спать" 3 секунды


if __name__ == '__main__':
    # Список имен для процессов
    process_names = [
        "Чебурек", "Банан", "Ёжик", "Пельмень", "Краб",
        "Пингвин", "Дыня", "Лимон", "Шаурма", "Слон",
        "Кот", "Тигр", "Ананас", "Гриб", "Змея",
        "Крокодил", "Мандарин", "Томат", "Кофе", "Огурец",
        "Бобр", "Хомяк", "Тюлень", "Воробей", "Лиса",
        "Медведь", "Гусь", "Киви", "Черепаха", "Павлин"
    ]

    # Создайте процессы с именами из списка
    processes = [multiprocessing.Process(target=task, name=name) for name in process_names]

    # Ниже реализуйте остальную логику
    for process in processes:
        process.start()

    kill_processes_by_names(target_names)

    for process in processes:
        process.join()
