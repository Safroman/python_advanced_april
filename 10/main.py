"""1) Написать REST для блога (использовать валидацию). Реализовать
модель Пост (название, содержание, дата публикации, автор, кол-во
просмотров, тег). Реализовать модель тег. Реализовать модель автор (имя,
фамилия, кол-во публикаций автора). Добавить валидацию ко всем полям.
Реализовать модуль заполнения всех полей БД валидными (адеквадными
данными :) ). Добавить вывод всех постов по тегу, при каждом обращении к
конкретному посту увеличовать кол-во просмотров на 1. При обращении к
автору, выводить все его публикации."""


from flask import Flask
from flask_restful import Api
from resources import *


app = Flask(__name__)
api = Api(app)

api.add_resource(AuthorResource, '/authors', '/authors/<author_id>')
api.add_resource(TagResource, '/tags', '/tags/<tag_id>')
api.add_resource(PostResource, '/new_post/<author_id>', '/new_post/<author_id>/<tag_id>', '/posts/<post_id>')


app.run(debug=True)

