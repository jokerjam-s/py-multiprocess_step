"""
Напишите код, который реализует передачу данных между двумя процессами с использованием одностороннего канала связи Pipe.
Один процесс выступает в роли отправителя данных, другой – в роли получателя. Отправитель генерирует набор чисел
и отправляет их по каналу, а получатель принимает и выводит эти данные на экран.
"""
import multiprocessing

def sender(connection):
    numbers = [x for x in range(50, 100, 7)]
    print("Отправитель начал отправку чисел.")
    for number in numbers:
        connection.send(number)
    connection.send(None)
    connection.close()

def receiver(connection):
    print("Получатель ожидает данные.")
    while number := connection.recv():
        print(f"Получено число: {number}")
    connection.close()
    print("Получение данных завершено.")


if __name__ == "__main__":
    # Создайте односторонний канал
    conn1, conn2 = multiprocessing.Pipe(duplex=False)

    # Создайте 2 процесса
    process1 = multiprocessing.Process(target=sender, args=(conn2,))
    process2 = multiprocessing.Process(target=receiver, args=(conn1,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()