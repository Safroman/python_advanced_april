"""1) Создать свою структуру данных Список, которая поддерживает индексацию.
Методы pop, append, insert, remove, clear. Перегрузить операцию сложения для списков,
которая возвращает новый расширенный объект."""


class CustomList:

    def __init__(self, *args):
        self._list = [el for el in args]

    def __str__(self):
        return f'{self._list}'

    def __setitem__(self, index, value):
        self._list[index] = value

    def __getitem__(self, index):
        return self._list[index]

    @property
    def list(self):
        return self._list

    def pop(self, i=-1):
        val = self._list[i]
        del self._list[i]
        return val

    def append(self, value):
        new = [value, ]
        self._list.extend(new)

    def insert(self, i, value):
        new_list = self._list[:i]
        new_list.extend([value, ])
        new_list.extend(self._list[i:])
        self._list = new_list

    def remove(self, val):
        for num, el in enumerate(self._list):
            if el == val:
                del self._list[num]
                break

    def clear(self):
        self._list = []

    def __add__(self, other):
        new_list = self._list.copy()
        new_list.extend(other.list)
        return CustomList(*new_list)
