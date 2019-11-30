class myclass:
    def test(self, x):
        self.x = x

    def __init__(self, x):
        self.x = x

    def addxwithSomething(self, z):
        print(self.x)
        self.x = self.x + z

    @staticmethod
    def static2plus2():
        return 4



print(myclass.static2plus2())

t1 = myclass(1)
print(t1.x)
t1.addxwithSomething(2)
print(t1.x)