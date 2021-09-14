from contextlib import suppress
from itertools import chain


class Array:
    def __new__(cls, *args):
        print('Class creation...')
        return super(Array, cls).__new__(cls)

    def __init__(self, initial_elements=None):
        array = [] if initial_elements is None else list(initial_elements)
        self.__dict__['array'] = array
        self.__dict__['named_elements'] = dict()

    def __del__(self):
        print('Class deleted.')

    def __str__(self):
        return f'Array: [{", ".join(map(str, self.array))}]'

    __repr__ = __str__

    def __iadd__(self, other):
        try:
            iter(other)
            for new_element in other:
                self.array.append(new_element)
        except TypeError:
            self.array.append(other)
        return self

    def __add__(self, other):
        try:
            iter(other)
            resulting_array = [el for el in chain(self.array, other)]
            return Array(resulting_array)
        except TypeError:
            return Array(self.array + [other])

    def __radd__(self, other):
        try:
            iter(other)
            resulting_array = [el for el in chain(other, self.array)]
            return Array(resulting_array)
        except TypeError:
            return Array([other] + self.array)

    def __len__(self):
        return len(self.array)

    def __iter__(self):
        return (el for el in self.array)

    def __eq__(self, other):
        try:
            if len(other) == len(self):
                return all(slf == oth for slf, oth in zip(self, other))
            else:
                return False
        except TypeError:
            return False

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return self == other or self > other

    def __bool__(self):
        return bool(self.array)

    def __setattr__(self, name, value):
        if value in self.array:
            self.named_elements[name] = self.array.index(value)
        else:
            self.array.append(value)
            self.named_elements[name] = len(self.array) - 1

    def __getattr__(self, item):
        if item in self.named_elements:
            index = self.named_elements[item]
            return self.array[index]
        else:
            super().__getattribute__(item)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.array[item]
        elif item in self.named_elements:
            index = self.named_elements[item]
            return self.array[index]
        else:
            raise KeyError('No such item')


a = Array([1, 2, 3])
a += [4, 5]
a += 6
b = a + (7, 8)
c = a + 9
d = (10, 11) + a
e = 12 + a

a1 = Array([1, 2, 3])
a2 = Array([1, 2, 3])
a3 = Array([1, 2, 3, 4])
b1 = a1 == a2
b2 = a1 == a3
b3 = a1 > a2
b4 = a1 < a3
b5 = a2 <= a1

a.key_number = 42
a.friday = 5
print(a.friday)
print(a.__add__(1))
try: print(a.wednesday)
except AttributeError: pass
pass

print(a[1])
print(a['friday'])
try: print(a['wednesday'])
except KeyError: pass
