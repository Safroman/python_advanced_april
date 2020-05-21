"""3) Написать свой контекстный менеджер для работы с файлами."""


class MySimpleContextManager:
    pass

    def __init__(self, name, mode):
        self._name = name
        self._mode = mode
        self._file = open(self._name, self._mode)

    def __enter__(self):
        print(f'file {self._name} was opened')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
        print(f'file {self._name} was closed')

    def read(self, n=None):
        if n is None:
            return self._file.read()
        else:
            return self._file.read(n)

    def write(self, text):
        self._file.write(text)


with MySimpleContextManager('test.txt', 'w') as file:
    print(type(file))
    file.write('bla')

with MySimpleContextManager('test.txt', 'r') as file:
    print(file.read())
