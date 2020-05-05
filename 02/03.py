class Point:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        return f'{self._x}, {self._y}, {self._z}'

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_z(self):
        return self._z

    def set_z(self, z):
        self._z = z

    def __add__(self, other):
        self._x += other.get_x()
        self._y += other.get_y()
        self._z += other.get_z()

    def __sub__(self, other):
        self._x -= other.get_x()
        self._y -= other.get_y()
        self._z -= other.get_z()

    def __mul__(self, other):
        self._x *= other.get_x()
        self._y *= other.get_y()
        self._z *= other.get_z()

    def __truediv__(self, other):
        if self._x % other.get_x() == 0:
            self._x //= other.get_x()
        else:
            self._x /= other.get_x()
        if self._y % other.get_y() == 0:
            self._y //= other.get_y()
        else:
            self._y /= other.get_y()
        if self._z % other.get_z() == 0:
            self._z //= other.get_z()
        else:
            self._z /= other.get_z()

    def __neg__(self):
        self._x = -self._x
        self._y = -self._y
        self._z = -self._z
        return f'{self}'

#        return -self._x, -self._y, -self._z


point1 = Point(2, 4, 6)
point2 = Point(2, 2, 2)


point1 + point2
print(point1)

point1 - point2
print(point1)

point1 * point2
print(point1)

point1 / point2
print(point1)

print(-point2)

