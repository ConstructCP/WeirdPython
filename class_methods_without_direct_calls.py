class C:
    def __init__(self):
        self.i = 42
        self.s = 'Hello'

    def i_plus(self, add):
        self.i += add

    def print(self):
        print(self.s + str(self.i))


c = C.__call__()
print(c.__dict__['i'])  # 42
c.__class__.__dict__['i_plus'](c, 1)  # i becomes 43
c.__class__.__dict__['print'](c)  # Hello43
