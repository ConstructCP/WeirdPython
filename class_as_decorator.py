class Logger:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args):
        print('Calling function: ' + self.fn.__name__)
        print('Arguments: ' + ', '.join(map(str, args)))
        res = self.fn(*args)
        print('Result: ' + str(res) + '\n')
        return res


class LoggerWithParams:
    def __init__(self, log):
        self.log = log

    def __call__(self, fn):
        def wrapper(*args):
            if self.log:
                print('Calling function: ' + fn.__name__)
                print('Arguments: ' + ', '.join(map(str, args)))
            res = fn(*args)
            if self.log:
                print('Result: ' + str(res) + '\n')
            return res
        return wrapper


class LoggerOptionalParams:
    def __init__(self, arg):
        self.fn = arg if callable(arg) else None
        self.log = arg if self.fn is None else True

    def __call__(self, *args):
        if self.fn is not None:
            res = self.wrapper(*args)
            return res
        else:
            self.fn = args[0]
            return self.wrapper

    def wrapper(self, *args):
        if self.log:
            print('Calling function: ' + self.fn.__name__)
            print('Arguments: ' + ', '.join(map(str, args)))
        res = self.fn(*args)
        if self.log:
            print('Result: ' + str(res) + '\n')
        return res




@Logger
def add1(x, y): return x + y

@LoggerWithParams(True)
def add2(x, y): return x + y

@LoggerWithParams(False)
def add3(x, y): return x + y

@LoggerOptionalParams
def add4(x, y): return x + y

@LoggerOptionalParams(True)
def add5(x, y): return x + y

@LoggerOptionalParams(False)
def add6(x, y): return x + y


add1(1, 1)
add2(2, 2)
add3(3, 3)
add4(4, 4)
add5(5, 5)
add6(6, 6)