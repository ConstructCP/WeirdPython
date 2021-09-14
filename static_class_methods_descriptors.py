class StaticMethod:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        return self.fn


class ClassMethod:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        def new_fn(*args):
            return self.fn(owner, *args)
        return new_fn


keys = ('id', 'name')


def from_dict(cls, dictionary):
    if all(key in dictionary for key in keys):
        return cls(dictionary['id'], dictionary['name'])


def hello_world():
    print('Hello world')


class C:
    def __init__(self, instance_id, name):
        self.id = instance_id
        self.name = name

    def __str__(self):
        return f'#{self.id} - {self.name}'

    hello = StaticMethod(hello_world)

    init_from_dict = ClassMethod(from_dict)


c1 = C(1, 'Raoul Duke')
c2 = C.init_from_dict({'id': 2, 'name': 'Hunter Thompson'})
print(c1)
print(c2)
c1.hello()
