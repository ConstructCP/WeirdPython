class C:
    x = 1

    def what_is_x(self):
        print(self.x)

    def change_x(self, new_x):
        self.__class__.x = new_x


c = C()
c.what_is_x()  # 1
c.change_x(42)
c.what_is_x()  # 42

cc = C()
c.what_is_x()  # 42
cc.change_x(100)
c.what_is_x()  # 100
