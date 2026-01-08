# Exercise 1: Recognize Obsolete Patterns
# For each code snippet, identify if it’s using an obsolete pattern that could be simplified:


# A
class Circle:
    pass


class Square:
    pass


class ShapeFactory:
    def create_shape(self, type):
        if type == "circle":
            return Circle()
        elif type == "square":
            return Square()


# B
def create_shape(type):
    shapes = {"circle": Circle, "square": Square}
    return shapes[type]()


# C
class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result


# D
def iterate(data):
    for item in data:
        yield item
