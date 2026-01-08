import sqlite3
from sqlite3 import Connection
from typing import Callable


class DataViewer:
    def __init__(self, filename: str, factory: Callable[[str], Connection]):
        self.connection = factory(filename)


def make_sqlite_connection(filename: str) -> Connection:
    filename = filename.strip()
    return sqlite3.connect(filename)


# Using the class directly as a factory (if it matched the signature)
# or using the helper function:
viewer1 = DataViewer("mydb.db", make_sqlite_connection)

# Or using a lambda for a quick fix
viewer2 = DataViewer("mydb.db", lambda f: sqlite3.connect(f.strip()))
