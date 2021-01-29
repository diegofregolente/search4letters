class CountFromBy:
    def __init__(self, v=0, i=1) -> None:
        self.val = v
        self.incr = i
        pass

    def increase(self) -> None:
        self.val += self.incr
        pass

    def __repr__(self) -> str:
        return str(self.val)
        pass


a = CountFromBy()
a.increase()
print(a, '\n')

b = CountFromBy(10, 5)
for n in range(4):
    b.increase()
print(b, '\n')

c = CountFromBy(500, 50)
print(c.val)
print(c.incr)
c.increase()
print(c)
