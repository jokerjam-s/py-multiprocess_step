import time
import multiprocessing


# Функция, выполняемая процессом
def process_task():
    time.sleep(1)


# Функция поиска и завершения процесса по его имени
def kill_process_by_name(target_name: str):
    child_process = multiprocessing.active_children()
    for proc in child_process:
        if proc.name == target_name:
            print(f"Процесс {proc.name} найден и будет завершен.")
            proc.kill()
            break
    else:
        print(f"Процесс {target_name} не найден.")



if __name__ == '__main__':
    # Список имен для дочерних процессов
    process_names = ["Чебурек", "Банан", "Ёжик", "Пельмень", "Краб", "Пингвин", "Дыня", "Лимон", "Шаурма", "Слон"]

    # Создайте и запустите процессы с именами из списка
    processes = [multiprocessing.Process(target=process_task, name=process_name) for process_name in process_names]

    for process in processes:
        process.start()

    # Внимание! Функцию kill_process_by_name(name) не вызывать! Завершения процессов не ждать!
