import multiprocessing
import os

# Определите количество логических ядер с помощью multiprocessing или os.
# Присвойте полученное значение переменной cpu_count, принтовать её не нужно
cpu_count = os.cpu_count()

print(cpu_count)