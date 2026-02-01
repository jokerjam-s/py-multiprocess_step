from multiprocessing import Process


def square(numbers: list):
    for n in numbers:
        print(f'{n}^2 = {n ** 2}')


def cube(numbers: list):
    for n in numbers:
        print(f'{n}^3 = {n ** 3}')


if __name__ == '__main__':
    numbers = [11, 22, 33, 44, 55]

    process1 = Process(target=square, args=(numbers,))
    process2 = Process(target=cube, args=(numbers,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
   