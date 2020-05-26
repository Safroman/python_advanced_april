"""1) Создать консольную программу-парсер, с выводом прогноза погоды. Дать возможность
пользователю получить прогноз погоды в его локации ( по умолчанию) и в выбраной локации,
на определенную пользователем дату. Можно реализовать, как консольную программу, так и веб страницу.
Используемые инструменты: requests, beautiful soup, остальное по желанию.
На выбор можно спарсить страницу, либо же использовать какой-либо API."""
import requests
from bs4 import BeautifulSoup
from datetime import datetime


SITE = 'https://sinoptik.ua/'
default_city = 'киев'

base_date = datetime.date(datetime.today())
active_date = base_date


def get_soup(city, date=None):

    if date is None:
        date = ''
    link = f'{SITE}погода-{city}'
    resp = requests.get(link)

    while resp.status_code != 200:
        print(f'прогноз для города {city} не доступен.')
        city = input('Введите другой город: ')
        link = f'{SITE}погода-{city}'
        resp = requests.get(link)

    link = f'{SITE}погода-{city}/{date}'
    resp = requests.get(link)
    while resp.status_code != 200:
        print(f'прогноз для города {city} на {date} не доступен.')
        date = input('Введите другую дату: ')
        link = f'{SITE}погода-{city}/{date}'
        resp = requests.get(link)

    if active_date < base_date:
        link = f'{SITE}погода-{city}/{date}'
    else:
        link = f'{SITE}погода-{city}/10-дней'
    resp = requests.get(link)

    return city, BeautifulSoup(resp.text, 'lxml')


def show_f_descr(s, d):

    if d == base_date:
        print('\nПрогноз погоды на сегодня:')
    elif d < base_date:
        print(f'Погода на {d}:')

    desc_par = {'class': 'wDescription clearfix'}
    short_desc = s.find('div', desc_par)
    desc_par2 = {'class': 'description'}
    s_desc = short_desc.find('div', desc_par2)
    print(s_desc.text)

    # min/max temp
    temp_p = {'class': 'temperature'}

    temp_min = s.find('tr', temp_p)
    t_min = int(temp_min.contents[9].text[0:-1])
    temp_max = s.find('tr', temp_p)
    t_max = int(temp_max.contents[11].text[0:-1])

    temp_f = {'class': 'temperatureSens'}

    temp_f_min = s.find('tr', temp_f)
    t_f_min = int(temp_f_min.contents[9].text[0:-1])
    temp_f_max = s.find('tr', temp_f)
    t_f_max = int(temp_f_max.contents[11].text[0:-1])

    print(f'Температура днем в среднем {(t_min + t_max) / 2:.0f}°')
    print(f'Ощущается как {(t_f_min + t_f_max) / 2:.0f}°')


def show_s_descr(s, d):

    # city/date
    city_par = {'class': 'cityName cityNameShort'}
    city = s.find('div', city_par)
    print(f"\nПогода {city.text.split(' ')[3]} {city.text.split(' ')[4]} на {active_date}:")

    diff = d - base_date
    n = diff.days
    id_p = f'bd{n+1}'

    # weather short
    par = {'class': 'tabs'}
    day = soup.find('div', par).findNext('div', id=id_p)
    # day = days.find('div', id=id_p)
    print(day.find('div')['title'])

    # temp
    temp_p = {'class': 'temperature'}
    temp_p_min = {'class': 'min'}
    temp_p_max = {'class': 'max'}

    temp_min = day.find('div', temp_p).findNext('div', temp_p_min).contents[1].text
    temp_max = day.find('div', temp_p).findNext('div', temp_p_max).contents[1].text

    print(f'Температура воздуха от {temp_min} до {temp_max}')


active_city, soup = get_soup(default_city)
show_f_descr(soup, active_date)

POS_ANS = {'1': 'посмотреть прогноз для другого города',
           '2': 'посмотреть прогноз на другую дату',
           '3': 'закончить'}
ans = ''

while ans != '3':
    print('\nвозможные действия:')
    for key, value in POS_ANS.items():
        print(key, ':', value)

    ans = input('выбери действие: ')

    if ans not in POS_ANS.keys():
        print('выбери действие из доступных!')

    elif ans == '1':
        active_city = input('введи название города:')

        if active_date <= base_date:
            active_city, soup = get_soup(active_city, active_date)
            show_f_descr(soup, active_date)
        else:
            active_city, soup = get_soup(active_city, active_date)
            show_s_descr(soup, active_date)

    elif ans == '2':
        new_date = datetime.date(datetime.strptime(input('введи дату в формате("ГГГГ-ММ-ДД"):'), "%Y-%m-%d"))

        if (new_date - base_date).days > 9:
            print('синоптики так далеко не загадывают')
        elif new_date <= base_date:
            active_date = new_date
            active_city, soup = get_soup(active_city, active_date)
            show_f_descr(soup, active_date)
        else:
            active_date = new_date
            active_city, soup = get_soup(active_city, active_date)
            show_s_descr(soup, active_date)
