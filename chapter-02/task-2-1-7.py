from multiprocessing import current_process

# получение экземпляра текущего процесса
main_process = current_process()

# вывод информации о типе процесса
print(type(main_process))