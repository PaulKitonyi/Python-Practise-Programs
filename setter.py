class calc:
    MULTI = 10
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @property
    def add(self):
        return self.x + self.y

    @property
    def subtract(self):
        return self.x - self.y

    @property
    def multiply(self):
        return self.x * self.y

    @staticmethod
    def sub(x,y):
        return y-x

    @classmethod
    def pau(cls,p):
        return cls.MULTI * p

    @property
    def values(self):
        return (self.x, self.y)

    @values.setter
    def values(self,tup):
        self.x , self.y = tup
        

num1 = calc(5,4)

print(num1.add)
print(num1.subtract)
print(num1.multiply)
print(num1.sub)
print(num1.pau(3))
num1.values = (6,7)
print(num1.add)
print(num1.subtract)
print(num1.multiply)
print(num1.values)