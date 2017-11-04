# Strange useless class, no comments
class Difference:
    def __init__(self, *args):
        if len(args) > 1:
            self.res = - args[-1].evaluate()
            for i in range(len(args) - 1):
                self.res += args[i].evaluate()
        else:
            self.res = -args[0]

    def evaluate(self):
        return self.res

a = Difference(5)
print(a.evaluate())
b = Difference(12)
c = Difference(a, b)
d = Difference(a, b, c)
print(c.evaluate())
print(d.evaluate())
print(a.evaluate())