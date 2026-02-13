"""
Напишите код, в котором два процесса будут обмениваться приветствиями через двусторонний канал связи.
Каждый процесс сначала отправляет сообщение другому процессу, а затем получает ответ.
После обмена сообщениями оба процесса завершаются.

Используйте двусторонний канал multiprocessing.Pipe() для организации обмена данными между процессами.
Первый процесс отправляет приветствие, получает ответ от второго процесса и выводит оба сообщения на экран.
Второй процесс получает приветствие от первого процесса, отправляет свой ответ и также выводит оба сообщения на экран.
"""
import multiprocessing


# Процесс 1: Отправляет приветствие и получает ответ
def process_1(connection):
    greeting_1 = "Привет из галактики Процесса 1!"
    connection.send(greeting_1)
    message = connection.recv()
    print(f"Процесс 1 отправил: {greeting_1}")
    print(f"Процесс 1 получил: {message}")


# Процесс 2: Получает приветствие и отправляет ответ
def process_2(connection):
    greeting_2 = "Процесс 2 на связи! Ускоряемся до световой скорости!"
    message = connection.recv()
    connection.send(greeting_2)
    print(f"Процесс 2 получил: {message}")
    print(f"Процесс 2 отправил: {greeting_2}")


if __name__ == "__main__":
    # Создание двустороннего канала связи
    conn1, conn2 = multiprocessing.Pipe()

    # Создание процессов
    process1 = multiprocessing.Process(target=process_1, args=(conn1,))
    process2 = multiprocessing.Process(target=process_2, args=(conn2,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()