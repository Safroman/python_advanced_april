"""Реализовать REST интернет магазина. Модель товар (цена,
доступность, кол-во доступных единиц, категория, кол-во просмотров),
Категория (описание, название). При обращении к конкретному товару
увеличивать кол-во просмотров на 1. Добавить модуль для заполнения
БД валидными данными. Реализовать подкатегории ( доп. Бал). Добавить
роут, который выводит общую стоимость товаров в магазине."""


from flask import Flask
from flask_restful import Api
from HW_resources import *


app = Flask(__name__)
api = Api(app)

api.add_resource(CategoryResource, '/categories', '/categories/<category_id>')
api.add_resource(ItemResource, '/items/<category_id>', '/items/<category_id>/<item_id>')
api.add_resource(TotalResource, '/total')

if __name__ == '__main__':
    app.run(debug=True)



