import threading


class SequenceGenerator:

    _instance = {}
    __number = 0
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        print("Creating new instance")
        with cls._lock:
            if cls not in cls._instance:
                cls._instance[cls] = super().__new__(cls)
            return cls._instance[cls]

    def get_next_number(self):
        self.__number += 1
        return self.__number


one = SequenceGenerator().get_next_number()
two = SequenceGenerator().get_next_number()
three = SequenceGenerator().get_next_number()
sequence = SequenceGenerator()
foor = sequence.get_next_number()
print(f"Generated numbers: {one}, {two}, {three}, {foor}")
