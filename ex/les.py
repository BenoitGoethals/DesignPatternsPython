import functools

position = [0, 0]


def function_transform(func):
    #return lambda x, y: func(y, x)
    def transformed_func():
        global position
        x, y = position
        y += 1
        x,y = func(x,y)
        position = x, y
        print(position)
    return transformed_func

@function_transform
def up(x, y):
    return x, y + 1
@function_transform
def right(x, y):
    return x + 1, y





up()
right()
right()

def check_positief(func):
    @functools.wraps(func)
    def wrapper(*args):
        for arg in args:
            if arg < 0:
              raise ValueError("Position is negative")
        return func(*args)
    return wrapper


@check_positief
def som(*args):
    return sum(args)


print(som(1,2,3))
#print(som(1,2,-3))

def add_url(cls):
    cls.url = "https://www.python.org"
    return cls

def add_url_extra(extra:str):
    def wrapper(cls):
        cls.url = f"{cls.url}/{extra}"
        return cls
    return wrapper



@add_url_extra("wuke")
@add_url
class Tempature:
    def __init__(self, temp):
        self.temp = temp




t= Tempature(10)
print(t.temp)
print(t.url)


