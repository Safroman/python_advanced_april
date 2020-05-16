import datetime


class User:

    credentials = {}
    population = {}

    def __init__(self, name, password, role='user'):
        self._u_name = name
        self._u_pw = password
        self._role = role
        self._reg_date = datetime.date.today()
        self._posts = []
        User.credentials[name] = password
        User.population[name] = self

    def __str__(self):
        return f'user {self._u_name}'

    @property
    def u_name(self):
        return self._u_name

    @property
    def u_pw(self):
        return self._u_pw

    @property
    def role(self):
        return self._role

    @property
    def reg_date(self):
        return self._reg_date

    @property
    def posts(self):
        return self._posts

    def new_post(self, post):
        self._posts.append(post)
