class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = self.function(obj)
        setattr(obj, self.name, value)
        return value


class DataLoader:
    @LazyProperty
    def data(self):
        print("Loading data...")
        return [1, 2, 3, 4, 5]
