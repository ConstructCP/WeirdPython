class ErrorSkip:
    def __init__(self, suppress_exceptions=True):
        self.suppress_exceptions = suppress_exceptions

    def __enter__(self):
        print('Enter CM')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('Exit CM without exception')
        else:
            print(f'Exception {exc_type}: {exc_val} [{exc_tb}]')
            if self.suppress_exceptions:
                return True
            return False


with ErrorSkip():
    assert None, "assert None"


with ErrorSkip(True):
    42 / 0


with ErrorSkip(False):
    raise BaseException('EPIC FAIL')
