"""
2) Создать функцию, которая будет скачивать файл из интернета по ссылке,
повесить на неё созданный декоратор.
Создать список из 10 ссылок, по которым будет происходить скачивание.
Создать список потоков, отдельный поток, на каждую из ссылок.
Каждый поток должен сигнализировать, о том, что, он начал работу и по какой
ссылке он работает, так же должен сообщать когда скачивание закончится.
"""
import requests
from threading import Thread


url_list = [
    'https://avto.informator.ua/wp-content/uploads/2019/05/Ferrari-288-GTO.jpg',
    'https://avto.informator.ua/wp-content/uploads/2019/05/Lamborghini-Miura.jpg',
    'https://avto.informator.ua/wp-content/uploads/2019/05/Lancia-Stratos.jpg',
    'https://avto.informator.ua/wp-content/uploads/2019/05/Porsche-911-Singer.jpg',
    'https://avto.informator.ua/wp-content/uploads/2019/05/BMW-i8.jpg',
    'https://avto.informator.ua/wp-content/uploads/2019/05/Land-Rover-Defender.jpg',
    'https://avto.informator.ua/wp-content/uploads/2019/05/Citroen-DS-D-capotable.jpeg',
    'https://avto.informator.ua/wp-content/uploads/2019/05/Fiat-500.jpg',
    'https://avto.informator.ua/wp-content/uploads/2019/05/Ford-Escort-Mexico.jpg',
    'https://avto.informator.ua/wp-content/uploads/2019/05/Ariel-Nomad.jpg']

t_list = [el.split('/')[-1] for el in url_list]


def outer_thread_decorator(d_type):

    def thread_decorator(func):

        def wrapper(url):
            t_name = url.split('/')[-1].split('.')[0]
            print(f'thread {t_name} started downloading from {url}')

            t = Thread(target=func, args=(url, ), name=t_name, daemon=d_type)
            t.start()

        return wrapper

    return thread_decorator


@outer_thread_decorator(False)
def download_pic(url):
    data = requests.get(url)
    name = url.split('/')[-1]

    with open(name, 'bw') as file:
        for line in data.iter_content(4096):
            file.write(line)

    print('download complete')


for i in range(len(url_list)):
    link = url_list[i]
    download_pic(link)
