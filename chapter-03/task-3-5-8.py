"""
Напишите код, который с помощью четырёх процессов последовательно собирает строку, передавая данные от одного процесса
к другому через каналы Pipe. Каждый процесс добавляет свою часть предложения к полученной строке, и в итоге последний
процесс передаёт собранную строку обратно в основной процесс, где она выводится на экран.
"""
import multiprocessing

def process_1(conn1a):
    text = "Start: "
    print(f"Process 1: Отправлено слово '{text}'")
    conn1a.send(text)

def process_2(conn1b, conn2a):
    text = conn1b.recv()
    text += "Однажды храбрый программист "
    print(f"Process 2: Получено '{text}' и отправлено дальше")
    conn2a.send(text)


def process_3(conn2b, conn3a):
    text = conn2b.recv()
    text += "отправился в страну Python "
    print(f"Process 3: Получено '{text}' и отправлено дальше")
    conn3a.send(text)

def process_4(conn3b, conn4a):
    text = conn3b.recv()
    text += "и победил все ошибки!"
    print(f"Process 4: Получено '{text}' и отправлено в основной процесс")
    conn4a.send(text)

if __name__ == "__main__":
    # Создайте каналы для передачи данных между процессами
    conn1a, conn1b = multiprocessing.Pipe()      # Канал для передачи от process1 к process2
    conn2a, conn2b = multiprocessing.Pipe()      # Канал для передачи от process2 к process3
    conn3a, conn3b = multiprocessing.Pipe()      # Канал для передачи от process3 к process4
    conn4a, conn4b = multiprocessing.Pipe()      # Канал для передачи от process4 в основной процесс

    # Создайте процессы
    process1 = multiprocessing.Process(target=process_1, args=(conn1a,))
    process2 = multiprocessing.Process(target=process_2, args=(conn1b, conn2a))
    process3 = multiprocessing.Process(target=process_3, args=(conn2b, conn3a))
    process4 = multiprocessing.Process(target=process_4, args=(conn3b, conn4a))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    text = conn4b.recv()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print(f"Итоговая строка: {text}")