"""1) Создать декоратор, который будет запускать функцию в отдельном потоке.
Декоратор должен принимать следующие аргументы: название потока, является ли поток демоном."""
from threading import Thread
import time


def outer_thread_decorator(t_name, d_type):

    def thread_decorator(func):

        def wrapper(*args, **kwargs):

            t = Thread(target=func, args=args, kwargs=kwargs, name=t_name, daemon=d_type)
            t.start()

        return wrapper

    return thread_decorator


@ outer_thread_decorator('t_1', False)
def cpu_burn():
    print('burn_start')
    a = []
    for i in range(15_000_000):
        a.append(i)
    print('burn_end')


@ outer_thread_decorator('t_1', False)
def sleep(sec, text):
    print(f'{text}')
    time.sleep(sec)
    print('sleep_end')


print('main_start')
cpu_burn()
sleep(5, text='sleep_start')
time.sleep(1)
print('main_end')
