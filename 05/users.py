import shelve
from posts import get_posts


user_list = 'UsersDB'
population = {}


def populate():
    with shelve.open(user_list) as db:
        for value in db.values():
            user = User(value[0], value[1], value[2], value[3])
            population[user.u_name] = user


class User:

    def __init__(self, name, password, date, role='user'):
        self._u_name = name
        self._u_pw = password
        self._role = role
        self._reg_date = date
        self._posts = get_posts(self._u_name)

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


if __name__ == '__main__':
    with shelve.open(user_list) as db:
        db.clear()
