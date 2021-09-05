def logger_decorator(fn):
    def function_wrapper(*args):
        print('Function: ' + fn.__name__)
        print('Arguments: ' + ', '.join(str(a) for a in args))
        res = fn(*args)
        print('Result: ' + str(res) + '\n')
        return res
    return function_wrapper


def logger_decorator_with_parameters(log):
    def decoration_wrapper(fn):
        def function_wrapper(*args):
            if log:
                print('Function: ' + fn.__name__)
                print('Arguments: ' + ', '.join(str(a) for a in args))
            res = fn(*args)
            if log:
                print('Result: ' + str(res) + '\n')
            return res
        return function_wrapper
    return decoration_wrapper


def logger_decorator_with_optional_parameters(arg=True):
    fn = None

    def function_wrapper(*args):
        if log:
            print('Function: ' + fn.__name__)
            print('Arguments: ' + ', '.join(str(a) for a in args))
        res = fn(*args)
        if log:
            print('Result: ' + str(res) + '\n')
        return res

    if isinstance(arg, bool):
        log = arg

        def decoration_wrapper(function):
            nonlocal fn
            fn = function
            return function_wrapper
        return decoration_wrapper
    else:
        fn = arg
        log = True
        return function_wrapper


@logger_decorator
def add1(x, y): return x + y

@logger_decorator_with_parameters(True)
def add2(x, y): return x + y

@logger_decorator_with_parameters(False)
def add3(x, y): return x + y

@logger_decorator_with_optional_parameters
def add4(x, y): return x + y

@logger_decorator_with_optional_parameters(True)
def add5(x, y): return x + y

@logger_decorator_with_optional_parameters(False)
def add6(x, y): return x + y


add1(1, 1)
add2(2, 2)
add3(3, 3)
add4(4, 4)
add5(5, 5)
add6(6, 6)