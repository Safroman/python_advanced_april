class ComplexNum:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    def __str__(self):
        if self._b == 0:
            return f'{self._a}'
        elif self._a == 0:
            return f'{self._b}i'
        elif self._b < 0:
            return f'{self._a} - {abs(self._b)}i'
        else:
            return f'{self._a} + {self._b}i'

    def __add__(self, other):
        if other == 0:
            return ComplexNum(self._a, self._b)
        elif other is int() or type(other) != type(self):
            raise ValueError('Only "0" or other Complex Number can be added to Complex Number')
        else:
            return ComplexNum((self._a + other.a), (self._b + other.b))

    def __sub__(self, other):
        return ComplexNum((self._a - other.a), (self._b - other.b))

    def __mul__(self, other):
        if other == 1:
            return ComplexNum(self._a, self._b)
        if other == 0:
            return 0
        elif other is int() or type(other) != type(self):
            raise ValueError('Complex Number can be multiplied only by "0", "1" or other Complex Number')
        else:
            return ComplexNum((self._a * other.a - self._b * other.b), (self._b * other.a + self._a * other.b))

    def __truediv__(self, other):
        return ComplexNum((self._a * other.a + self._b * other.b) / (other.a ** 2 + other.b ** 2),
                          (self._b * other.a - self._a * other.b) / (other.a ** 2 + other.b ** 2))

