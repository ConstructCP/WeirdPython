import types


class Property:
    def __init__(self, getter_function):
        self.getter_function = getter_function
        self.setter_function = None
        self.deleter_function = None

    def __call__(self, *args, **kwargs):
        res = self.getter_function(*args, **kwargs)
        return res

    # def __get__(self, instance, owner):
    #     return self.getter_function
    #
    # def __set__(self, instance, value):
    #     if self.setter_function:
    #         return self.setter_function(value)
    #     else:
    #         raise AttributeError('Setting attribute is not supported')
    #
    # def __delete__(self, instance):
    #     if self.deleter_function:
    #         return self.deleter_function
    #     else:
    #         raise AttributeError('Deleting attribute is not supported')
    #
    # def setter(self, fn):
    #     self.setter_function = fn
    #     return self


class C:
    @Property
    def x(self):
        print('Get x')
    #
    # @x.setter
    # def x(self, value):
    #     print(f'Set x = {value}')


c = C()
pass


