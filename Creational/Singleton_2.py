def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class DatabaseConnection:
    def __init__(self):
        self.connection = "Connected to DB"

    def query(self, sql):
        return f"Executing: {sql}"


# Gebruik
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True