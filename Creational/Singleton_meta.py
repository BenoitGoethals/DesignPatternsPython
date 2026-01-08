class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DbConnection(metaclass=Singleton):
    def __init__(self):
        self._connection = "Connected to DB"

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, value):
        self._connection = value


dn1 = DbConnection()
dn1.connection = "Connected to DB2"
dn2 = DbConnection()
dn2.connection = "Connected to DB3"
print(dn1 is dn2)

print(dn1.connection)
print(dn2.connection)
