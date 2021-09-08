class C:
    __x = 10
    __x__ = 20
    __x_x = 30
    __x_x__ = 40
    _C__x = 50

    def __fn(self):
        print('__fn')

    def __fn__(self):
        print('__fn__')

    def __fn_fn(self):
        print('__fn_fn')

    def __fn_fn__(self):
        print('__fn_fn__')


c = C()
try:
    print(c.__x)
except AttributeError:
    print('Use as c._C__x')
try:
    print(c.__x_x)
except AttributeError:
    print('Use as c._C__x_x')
print(c._C__x)
print(c.__x__)
print(c._C__x_x)
print(c.__x_x__)

try:
    c.__fn()
except AttributeError:
    print('Use as c._C__fn()')
try:
    c.__fn_fn()
except AttributeError:
    print('Use as c._C__fn_fn()')
c._C__fn()
c.__fn__()
c._C__fn_fn()
c.__fn_fn__()
