from random import choice
from models import *


Author_names = ['Андрей', 'Егор', 'Илья']
Author_surnames = ['Сидоров', 'Петров', 'Иванов']

tag_list = ['спорт', 'наука', 'иcкуccтво', 'погода', 'кино']
title_list = ['Сенсация', 'Шок', 'Ураган', 'Прорыв', 'Позор']
text_list = ['текст 1', 'текст 2', 'текст 3', 'текст 4', 'текст 5']

for i in range(len(Author_names)):
    Author.create(**{'name': choice(Author_names), 'surname': choice(Author_surnames)})

for i in range(len(tag_list)):
    Tag.create(**{'tag': choice(tag_list)})

for i in range(len(title_list)):
    author = choice(Author.read())
    tag = choice(Tag.read())
    Post.create(author, tag, **{'title': choice(title_list), 'text': choice(text_list)})

