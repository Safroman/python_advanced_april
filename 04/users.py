import datetime


class User:

    credentials = {}
    population = {}

    def __init__(self, name, password, role='user'):
        self._name = name
        self._pw = password
        self._role = role
        self._reg_date = datetime.date.today()
        self._posts = []
        User.credentials[name] = password
        User.population[name] = self

    def __str__(self):
        return f'user {self._name}'

    @property
    def name(self):
        return self._name

    @property
    def pw(self):
        return self._pw

    @property
    def role(self):
        return self._role

    @property
    def reg_date(self):
        return self._reg_date

    @property
    def posts(self):
        return self._posts

    def add_post(self, post):
        self._posts.append(post)
