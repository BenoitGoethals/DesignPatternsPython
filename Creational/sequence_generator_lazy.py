import threading


class SequenceGenerator:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        # This check prevents re-initializing the counter if __init__ is called again
        if not hasattr(self, "_SequenceGenerator__number"):
            self.__number = 0

    @classmethod
    def get_instance(cls):
        # Double-checked locking for thread safety and performance
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print("Lazy initialization: Creating instance now.")
                    cls._instance = cls()
        return cls._instance

    def get_next_number(self):
        self.__number += 1
        return self.__number


if __name__ == "__main__":
    # The instance is NOT created until get_instance() is called
    print("Program started...")

    gen = SequenceGenerator.get_instance()
    print(f"Number: {gen.get_next_number()}")

    another_gen = SequenceGenerator.get_instance()
    print(f"Number: {another_gen.get_next_number()}")
