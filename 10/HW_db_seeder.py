from random import choice, randint
from HW_models import *
from mongoengine import *

connect('shop_db')

ITEMS = {
    'fruits': [
        'apple',
        'pear',
        'grape'],
    'vegetables': [
        'potato',
        'onion',
        'corn'],
    'sport goods': [
        'tennis ball',
        'skate',
        'bicycle']
    }


def seed_categories(n):

    cat_list = [key for key in ITEMS.keys()]
    created = []

    for i in range(n):
        params = {}

        category = choice(cat_list)
        while category in created:
            category = choice(cat_list)
        description = f'This category includes different {category}'
        params['title'] = category
        params['description'] = description
        Category.create(**params)
        created.append(category)


def seed_items():

    categories = Category.read()

    for cat in categories:
        items = ITEMS[cat['title']]

        for item in items:
            params = dict()
            params['name'] = item
            params['price'] = randint(1, 100) * 10
            params['availability'] = 1
            params['quantity'] = randint(1, 100)
            params['category'] = cat
            Item.create(**params)


seed_categories(3)
seed_items()

