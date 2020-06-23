from mongoengine import *
import datetime


connect('blog_db')


class Author(Document):

    name = StringField(required=True)
    surname = StringField(required=True)
    posts = IntField(default=0)

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def read(cls, author_id=None):
        if author_id:
            return cls.objects.get(id=author_id)
        else:
            return cls.objects.filter()

    def update(self, **kwargs):

        if 'name' in kwargs.keys():
            self.name = kwargs['name']
        if 'surname' in kwargs.keys():
            self.surname = kwargs['surname']
        self.save()
        return self

    @classmethod
    def delete(cls, author_id):
        cls.objects(id=author_id).delete()


class Tag(Document):

    tag = StringField()

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def read(cls, tag_id=None):
        if tag_id:
            res = cls.objects.get(id=tag_id)
        else:
            res = cls.objects.filter()
        return res

    def update(self, **kwargs):

        if 'tag' in kwargs.keys():
            self.tag = kwargs['tag']
        self.save()

    @classmethod
    def delete(cls, post_id):
        cls.objects(id=post_id).delete()


class Post(Document):

    title = StringField()
    text = StringField()
    date = DateTimeField(default=datetime.datetime.now())
    author = ReferenceField(Author)
    views = IntField(default=0)
    tag = ReferenceField('Tag')

    @classmethod
    def create(cls, author, tag=None, **kwargs):
        kwargs['author'] = author
        kwargs['tag'] = tag
        new_post = cls.objects.create(**kwargs)
        author.posts = len(cls.objects.filter(author=author))
        author.save()
        return new_post

    @classmethod
    def read(cls, post_id=None, author=None, tag=None):
        res = None
        if post_id:
            res = cls.objects.get(id=post_id)
            res.views += 1
            res.save()
        elif author:
            res = cls.objects.filter(author=author)
        elif tag:
            res = cls.objects.filter(tag=tag)
        return res

    def update(self, **kwargs):

        if 'title' in kwargs.keys():
            self.title = kwargs['title']
        if 'text' in kwargs.keys():
            self.text = kwargs['text']
        if 'date' in kwargs.keys():
            self.date = kwargs['date']
        if 'author' in kwargs.keys():
            self.author = kwargs['author']
        if 'views' in kwargs.keys():
            self.views = kwargs['views']
        if 'tag' in kwargs.keys():
            self.tag = kwargs['tag']
        self.save()
        return self

    @classmethod
    def delete(cls, post_id):
        cls.objects(id=post_id).delete()
