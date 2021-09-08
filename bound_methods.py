class A:
    def fn(self):
        print(f'Class {type(self).__name__}: in function fn' + '\n')


class B(A):
    def __getattribute__(self, item):
        print(f'Class B: Getting attribute {item}')
        return super().__getattribute__(item)


class C(A):
    def __getattribute__(self, item):
        print(f'Class C: Block getting attribute {item}')


class D(A):
    def say_hello(self):
        print('Hello world!')

    def __getattribute__(self, item):
        if item == 'say_hello':
            return super().__getattribute__(item)
        print(f'Class D: replacing function {item} with hello world')
        return self.say_hello


a = A()
b = B()
c = C()
d = D()

a.fn()
b.fn()
try: c.fn()
except TypeError: print('Bound method creation blocked\n')
d.fn()
