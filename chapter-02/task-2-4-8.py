import threading
import multiprocessing

# Получите текущий процесс и сохраните его в переменную process
process = multiprocessing.current_process()

# Получите главный поток и сохраните его в переменную main_thread
main_thread = threading.main_thread()

# Выведите детали
print(f"Процесс: {process.name}, главный поток: {main_thread.name}")

