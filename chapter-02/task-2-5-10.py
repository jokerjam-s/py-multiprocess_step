# Переменная search_name и её содержимое скрыто под капотом. Она содержит строку, имя процесса, который необходимо найти.
search_name = "Пельмень"
from multiprocessing.process import BaseProcess
import time
import multiprocessing


# Функция, выполняемая процессом
def process_task():
    time.sleep(1)


# Функция поиска процесса по имени
def get_process_by_name(search_name: str) -> BaseProcess | None:
    children_processes = multiprocessing.active_children()
    for proc in children_processes:
        if proc.name == search_name:
            return proc
    return None


if __name__ == '__main__':
    # Список имен процессов
    process_names = ["Чебурек", "Банан", "Ёжик", "Пельмень", "Краб", "Пингвин", "Дыня", "Лимон", "Шаурма", "Слон"]

    # Создайте и запустите процессы с именами из списка process_names
    processes = [multiprocessing.Process(target=process_task, name=process_name) for process_name in process_names]

    for process in processes:
        process.start()

    process = get_process_by_name(search_name)
    if process:
        print(f"Найден процесс: {process.name}")

    for process in processes:
        process.join()

