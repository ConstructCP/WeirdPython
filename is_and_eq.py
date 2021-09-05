"""
x = X()
y = Y()

print(x == y)  # -> True
print(y == x)  # -> False
print(x == x)  # -> True
print(y == y)  # -> False
"""


class X:
    def __eq__(self, other):
        if other is self:
            return True
        elif isinstance(other, Y):
            return True
        else:
            return False


class Y:
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if self is other:
            return False


x = X()
y = Y()

print(x == y)  # -> True
print(y == x)  # -> False
print(x == x)  # -> True
print(y == y)  # -> False