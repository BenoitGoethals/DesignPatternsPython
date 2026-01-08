import functools


def debugme(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}! { kwargs}")
        return func(*args, **kwargs)

    return wrapper


def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Function {func.__name__} has been called {wrapper.calls} times")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def time(func):
    import time

    start_time = time.time()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}!")

        return func(*args, **kwargs)

    end_time = time.time()
    print(f"Function {func.__name__} took {start_time - end_time} seconds to execute")
    return wrapper


@time
@counter
@debugme
def testcase(x="sdfdsfs", y="sfdsf", zip=2):
    print(x + y + str(zip))


testcase(zip=3)
testcase(zip=3)
testcase(zip=3)


def define_move(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global position
        x, y = position
        position = func(x, y)
        print(f"You are at coordinates {position}")

    return wrapper


@define_move
def up(x, y):
    return x, y + 1


@define_move
def right(x, y):
    return x + 1, y


@define_move
def down(x, y):
    return x, y - 1


@define_move
def left(x, y):
    return x - 1, y


position = [0, 0]
up()
up()
right()
up()
down()
left()


def deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}!")
        return func(*args, **kwargs)

    return wrapper


@deco
def test(x):
    """This function will take a number and double it"""
    return 2 * x


test(2)


def apply_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}!")
        return func(func(*args, **kwargs))

    return wrapper


@apply_twice
def add_five(x):
    return x + 5


print(add_five(3))
