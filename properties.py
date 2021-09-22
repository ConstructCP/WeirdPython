class C:
    def __init__(self):
        self._x = 10
        self._y = 20
        self._z = 30

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        print(f'Set c.x = {value}')
        self._x = value

    @x.deleter
    def x(self):
        print(f'Delete c.x')
        self.__dict__.pop('_x')

    def __get_y(self):
        return self._y

    def __set_y(self, value):
        print(f'Set c.y = {value}')
        self._y = value

    def __delete_y(self):
        print(f'Delete c.y')
        self.__dict__.pop('_y')

    y = property(__get_y, __set_y, __delete_y)

    @property
    def z(self):
        return 100

    @z.getter
    def z(self):
        return 200


c = C()
print(f'c.x -> {c.x}')
c.x = 42
print(f'c.x -> {c.x}')
try:
    del c.x
    print(c.x)
except AttributeError as e:
    print(f'c.x -> {e}')

print(f'c.y -> {c.y}')
c.y = 42
print(f'c.x -> {c.y}')
try:
    del c.y
    print(c.y)
except AttributeError as e:
    print(f'c.y -> {e}')

print(f'c.z -> {c.z}')
try:
    c.z = 300
except AttributeError as e:
    print(f'Set c.z -> {e}')
