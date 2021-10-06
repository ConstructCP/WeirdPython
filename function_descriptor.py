""" Emulating function descriptor which returns bound objects """
import types


class UsualMethod(object):
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return types.MethodType(self.fn, instance)


def hello_world(self):
    print(f'Hello world! {str(self)}')


def hello_name(self, name):
    print(f'Hello {name}! {str(self)}')


def greeter_str(self):
    return "This is just a greeter object."


class Greeter:
    hello = UsualMethod(hello_world)
    hello_name = UsualMethod(hello_name)
    __str__ = UsualMethod(greeter_str)


# just_hello = UsualMethod(hello_world)
# just_hello()
greeter = Greeter()
greeter.hello()
greeter.hello_name('dude')
print(greeter)
