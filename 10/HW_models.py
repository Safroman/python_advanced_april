from mongoengine import *
import copy


connect('shop_db')


class Category(Document):

    title = StringField(required=True)
    description = StringField(required=True)

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def read(cls, category_id=None):
        if category_id is None:
            return cls.objects
        else:
            return cls.objects.get(id=category_id)

    def update(self, **kwargs):
        if 'title' in kwargs.keys():
            self.title = kwargs['title']
        if 'description' in kwargs.keys():
            self.description = kwargs['description']
        self.save()

    @classmethod
    def delete(cls, category_id):
        cls.objects(id=category_id).delete()


class Item(Document):
    name = StringField(required=True)
    price = FloatField(required=True)
    availability = IntField(required=True)
    quantity = IntField(required=True)
    category = ReferenceField(Category)
    views = IntField(default=0)

    @classmethod
    def create(cls, category, **kwargs):
        data = dict(**kwargs)
        data['category'] = category
        return cls.objects.create(**data)

    @classmethod
    def read(cls, item_id):
        item = Item.objects.get(id=item_id)
        res = copy.copy(item)
        item.views += 1
        item.save()
        return res

    def update(self, category=None, **kwargs):

        if 'name' in kwargs.keys():
            self.name = kwargs['name']
        if 'price' in kwargs.keys():
            self.price = kwargs['price']
        if 'availability' in kwargs.keys():
            self.availability = kwargs['availability']
        if 'quantity' in kwargs.keys():
            self.quantity = kwargs['quantity']
        if category != self.category:
            self.category = category
        if 'views' in kwargs.keys():
            self.views = kwargs['views']

        self.save()

    @classmethod
    def delete(cls, item_id):
        cls.objects(id=item_id).delete()


class Total(Document):

    def read(self):
        total = 0
        items = Item.objects.filter()
        for item in items:
            total += item['price'] * item['quantity']

        res = {'total amount': total}
        return res
