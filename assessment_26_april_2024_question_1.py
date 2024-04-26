class BaseClass:
    def __init__(self,x):
        self.x = x

class AnotherBaseClass:
    def __init__(self,y):
        self.y = y


class MultipleInheritence(BaseClass, AnotherBaseClass):
    def __init__(self,x,y):
        BaseClass.__init__(self, x)
        AnotherBaseClass.__init__(self, y)

    @staticmethod
    def decorate(func):
        return lambda *args,**kwargs: func(*args,**kwargs) * 2

obj = MultipleInheritence(5,10)

@obj.decorate
def multiply(a, b):
    return a * b

result = multiply(obj.x, obj.y)
print(result)

