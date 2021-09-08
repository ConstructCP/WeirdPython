"""
class A:
  pass
A = foo(A)
"""


def create_logger_fun(cls):
    def inner(*args):
        print('Creating class ' + cls.__name__)
        print('Args: ' + ', '.join(map(str, args)) + '\n')
        return cls(*args)
    return inner


class create_logger_class:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args):
        print('Creating class ' + self.cls.__name__)
        print('Args: ' + ', '.join(map(str, args)) + '\n')
        return self.cls(*args)


class method_calls_decorated:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __getattr__(self, item):
        attr = getattr(self.instance, item)
        if not callable(attr):
            return attr
        else:
            return self.log_call(attr)

    def __call__(self, *args):
        print('Creating class ' + self.cls.__name__)
        print('Args: ' + ', '.join(map(str, args)) + '\n')
        self.instance = self.cls(*args)
        return self

    @staticmethod
    def log_call(fn):
        def inner(*args):
            print('Running method ' + fn.__name__)
            print('Args: ' + ', '.join(map(str, args)))
            res = fn(*args)
            print('Result: ' + str(res) + '\n')
            return res
        return inner



@create_logger_fun
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y


@create_logger_class
class B:
    def __init__(self, x, y):
        self.x = x
        self.y = y


@method_calls_decorated
class C:
    def hello(self):
        return 'Hello world'

    def hello_name(self, name):
        return 'Hello ' + str(name)


a = A(1, 2)
b = B(3, 4)
c = C()
c.hello()
c.hello_name(42)
pass
