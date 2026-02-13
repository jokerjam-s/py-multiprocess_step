"""
Напишите код, который создаёт два процесса, которые будут обмениваться сообщениями через канал связи (Pipe). Один процесс будет отправлять сообщение, а другой – принимать и выводить его на экран.

Создайте канал связи с помощью multiprocessing.Pipe().
Процесс 1 должен отправить текстовое сообщение в Процесс 2 через канал.
Процесс 2 должен получить это сообщение и вывести его на экран.
"""
import multiprocessing
from multiprocessing import Process


# Функция отправки сообщения через канал
def sender(connection):
    connection.send('Hello from Process 1!')

# Функция получение сообщения через канал
def receiver(connection):
    value = connection.recv()
    print(f"Получено сообщение:{value}")

if __name__ == "__main__":
    # Создание двустороннего канала связи
    conn1, conn2 = multiprocessing.Pipe()

    # Создание процессов
    process1 = Process(target=sender, args=(conn1,))
    process2 = Process(target=receiver, args=(conn2,))

    process1.start()
    process2.start()
    process1.join()
    process2.join()