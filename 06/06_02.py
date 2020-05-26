"""2) Создать свою структуру данных Словарь, которая поддерживает методы,
get, items, keys, values. Так же перегрузить операцию сложения для
словарей, которая возвращает новый расширенный объект."""


class CustomDict:

    def __init__(self, args):
        self._dict = dict(args)

    def __str__(self):
        return f'{self._dict}'

    def __setitem__(self, index, value):
        self._dict[index] = value

    def __getitem__(self, index):
        return self._dict[index]

    @property
    def dict(self):
        return self._dict

    def get(self, key):
        try:
            return self._dict[key]
        except KeyError:
            return None

    def items(self):
        for key in self._dict:
            yield key, self._dict[key]

    def keys(self):
        for key in self._dict:
            yield key

    def values(self):
        for key in self._dict:
            yield self._dict[key]

    def __add__(self, other):
        new_dict = []
        for key, value in self._dict.items():
            new_dict.append((key, value))
        for key, value in other.dict.items():
            new_dict.append((key, value))

        return CustomDict(new_dict)
