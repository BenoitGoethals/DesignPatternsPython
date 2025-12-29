class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.data = []
            self.initialized = True


# Gebruik
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True - beide verwijzen naar hetzelfde object

s1.data.append("test")
print(s2.data)  # ["test"] - gedeelde state