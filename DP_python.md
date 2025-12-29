# Complete Lijst van Design Patterns - Python Editie

Design patterns worden onderverdeeld in drie hoofdcategorieën: Creational, Structural en Behavioral patterns.

**Legenda:**
- 🐍 **Built-in Python** - Al ingebouwd in Python
- ⭐ **Veel gebruikt in Python** - Veelvoorkomend in Python code
- 🔧 **Pythonic alternatief** - Python heeft een eenvoudiger alternatief
- 📚 **Framework/Library** - Gebruikt in populaire Python frameworks

---

## Creational Patterns (Creatie)

### 1. **Singleton** 🔧
Zorgt ervoor dat een klasse slechts één instantie heeft.

**Python status:** Python heeft betere alternatieven
- Modules zijn al singletons
- `@functools.lru_cache` voor caching
- Metaclasses voor echte singletons

```python
# Pythonic alternatief: gewoon een module gebruiken
# config.py
database_url = "postgresql://..."
api_key = "secret"

# app.py
import config
print(config.database_url)  # Altijd dezelfde instantie
```

### 2. **Factory Method** ⭐📚
Definieert een interface voor het creëren van objecten.

**Python status:** Zeer veel gebruikt in frameworks zoals Django, Flask

```python
# Django gebruikt dit overal
from django.views import View  # Factory voor views
from rest_framework.serializers import ModelSerializer  # Factory voor serializers
```

### 3. **Abstract Factory** 📚
Families van gerelateerde objecten creëren.

**Python status:** Gebruikt in UI frameworks en cross-platform libraries

### 4. **Builder** ⭐
Complexe objecten stap voor stap bouwen.

**Python status:** Veel gebruikt, maar vaak vervangen door:
- Keyword arguments
- Dataclasses
- Pydantic models

```python
# Modern Python alternatief
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int = 18
    active: bool = True

# Simpel te gebruiken
user = User(name="Jan", email="jan@example.com", age=25)
```

### 5. **Prototype** 🐍
Objecten klonen.

**Python status:** Built-in via `copy` module

```python
import copy

original = {"name": "Jan", "scores": [1, 2, 3]}
shallow = copy.copy(original)       # Shallow copy
deep = copy.deepcopy(original)      # Deep copy
```

### 6. **Object Pool** 📚
Objecten hergebruiken in plaats van opnieuw creëren.

**Python status:** Gebruikt in database connection pools
- `psycopg2.pool`
- `SQLAlchemy` connection pooling
- `multiprocessing.Pool`

---

## Structural Patterns (Structuur)

### 7. **Adapter (Wrapper)** ⭐
Incompatibele interfaces laten samenwerken.

**Python status:** Zeer gebruikelijk, Python's duck typing maakt het natuurlijk

```python
# Python maakt adapters makkelijk
class EuropeanSocket:
    def voltage(self): return 230
    
class USASocketAdapter:
    def __init__(self, socket):
        self.socket = socket
    def voltage(self): return 110  # Aangepast
```

### 8. **Bridge** 📚
Abstractie scheiden van implementatie.

**Python status:** Gebruikt in database drivers (DB-API)

### 9. **Composite** ⭐
Tree structuren voor part-whole hiërarchieën.

**Python status:** Veel gebruikt in:
- File systems
- UI frameworks (tkinter, PyQt)
- AST (Abstract Syntax Trees)

### 10. **Decorator** 🐍⭐
Dynamisch functionaliteit toevoegen.

**Python status:** BUILT-IN met `@decorator` syntax!

```python
# Python's decorator syntax
@functools.lru_cache(maxsize=128)
@staticmethod
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

# Populaire decorators:
@property
@staticmethod
@classmethod
@dataclass
@functools.wraps
@contextlib.contextmanager
```

### 11. **Facade** ⭐📚
Vereenvoudigde interface naar complex systeem.

**Python status:** Overal in Python libraries
- `requests` library (facade over urllib3)
- `pathlib` (facade over os.path)
- `pandas` (facade over numpy)

### 12. **Flyweight** 🐍
Geheugen efficiënt delen van objecten.

**Python status:** Python doet dit automatisch!
- String interning: `a = "test"; b = "test"; a is b  # True`
- Integer caching: kleine integers (-5 tot 256)
- `sys.intern()` voor custom strings

### 13. **Proxy** ⭐🐍
Surrogaat voor toegangscontrole.

**Python status:** Veel gebruikt, Python heeft tools:
- `weakref.proxy()` voor weak references
- `__getattr__` en `__setattr__` voor custom proxies
- Property decorators

```python
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
```

### 14. **Private Class Data** 🐍
Data encapsulatie.

**Python status:** Python conventie met `_` en `__`
- `_private`: conventie voor intern gebruik
- `__private`: name mangling
- `@property` voor getters/setters

---

## Behavioral Patterns (Gedrag)

### 15. **Chain of Responsibility** ⭐📚
Request door ketting van handlers sturen.

**Python status:** Gebruikt in:
- Django middleware
- Flask before_request handlers
- Logging handlers

```python
# Python logging gebruikt dit
import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())  # Handler 1
logger.addHandler(logging.FileHandler('app.log'))  # Handler 2
```

### 16. **Command** ⭐
Requests inkapselen als objecten.

**Python status:** Zeer gebruikelijk
- Undo/redo systems
- Task queues (Celery)
- Click library voor CLI commands

### 17. **Interpreter** 📚
Taalgrammatica interpreteren.

**Python status:** Gebruikt in Python zelf!
- `ast` module (Abstract Syntax Trees)
- `re` module (regex)
- SQL parsers

### 18. **Iterator** 🐍⭐
Sequentiële toegang tot collecties.

**Python status:** BUILT-IN protocol!

```python
# Python's iterator protocol
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        raise StopIteration

# Of met generators (nog simpeler!)
def counter(max):
    current = 0
    while current < max:
        current += 1
        yield current

# Built-in itertools module!
from itertools import chain, cycle, islice
```

### 19. **Mediator** 📚
Interactie tussen objecten centraliseren.

**Python status:** Gebruikt in GUI frameworks en event systems

### 20. **Memento** ⭐
Toestand opslaan voor undo.

**Python status:** Veel gebruikt in:
- Pickle voor serialisatie
- `copy.deepcopy()` voor snapshots
- ORM state management

### 21. **Observer (Pub-Sub)** ⭐📚
Event notification systeem.

**Python status:** Zeer populair!
- Django signals
- PyQt signals/slots
- RxPY (Reactive Extensions)
- `asyncio` event loops

```python
# Django signals voorbeeld
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print(f"User {instance.name} was saved!")
```

### 22. **State** ⭐
Gedrag veranderen op basis van state.

**Python status:** Vaak gebruikt, libraries helpen:
- `transitions` library voor state machines
- `enum.Enum` voor states

```python
from enum import Enum

class State(Enum):
    IDLE = 1
    RUNNING = 2
    FINISHED = 3

class Process:
    def __init__(self):
        self.state = State.IDLE
```

### 23. **Strategy** ⭐🐍
Algoritmen uitwisselbaar maken.

**Python status:** Natuurlijk in Python met first-class functions!

```python
# Strategy pattern in Python = gewoon functies doorgeven!
def bubble_sort(data): 
    pass

def quick_sort(data): 
    pass

def sort_data(data, strategy=quick_sort):
    return strategy(data)

# Of met dictionary
strategies = {
    'bubble': bubble_sort,
    'quick': quick_sort
}
```

### 24. **Template Method** ⭐📚
Algoritme skelet in base class.

**Python status:** Veel gebruikt in frameworks
- Django class-based views
- unittest.TestCase

```python
class BaseView:
    def dispatch(self):
        self.setup()
        response = self.handle()
        return self.finalize(response)
    
    def setup(self): pass
    def handle(self): raise NotImplementedError
    def finalize(self, response): return response
```

### 25. **Visitor** 📚
Operaties op object structuren.

**Python status:** Gebruikt in AST manipulation, maar vaak vervangen door functional approaches

### 26. **Null Object** 🔧
Default object in plaats van None.

**Python status:** Python heeft betere alternatieven
- `None` is expliciet en Pythonic
- `or` operator: `value = input or default`
- `collections.defaultdict`

---

## Concurrency Patterns

### 27-31. **Concurrency Patterns** 🐍⭐
**Python status:** Python heeft uitgebreide built-in support!

```python
# Threading
import threading
lock = threading.Lock()
with lock:  # Monitor Object pattern
    # Thread-safe code
    pass

# Multiprocessing
from multiprocessing import Pool
with Pool(4) as pool:  # Thread Pool pattern
    results = pool.map(function, data)

# Asyncio (modern Python)
import asyncio

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(process_data())
    await asyncio.gather(task1, task2)

asyncio.run(main())

# Threading utilities
from threading import RLock  # Reentrant Lock
from threading import Semaphore  # Semaphore
from concurrent.futures import ThreadPoolExecutor  # Thread Pool
```

---

## Architectural Patterns

### 32. **MVC** 📚
Model-View-Controller.

**Python status:** Basis van Django!
- Model: `models.py`
- View: `views.py` (eigenlijk Controller)
- Template: HTML templates (eigenlijk View)

### 33. **MVVM** 📚
**Python status:** Gebruikt in moderne UI frameworks (Kivy)

### 34. **MVP** 📚
**Python status:** Minder gebruikelijk in Python

### 35. **Dependency Injection** ⭐
**Python status:** Zeer populair!
- FastAPI gebruikt het uitgebreid
- `dependency-injector` library
- Type hints maken DI natuurlijk

```python
# FastAPI dependency injection
from fastapi import Depends

def get_db():
    db = Database()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def get_users(db: Database = Depends(get_db)):
    return db.query(User).all()
```

### 36. **Repository** ⭐📚
**Python status:** Gebruikt in alle ORM frameworks
- SQLAlchemy
- Django ORM
- Peewee

### 37. **Service Locator** 🔧
**Python status:** Python gebruikt meestal DI in plaats hiervan

---

## Enterprise Patterns

### 38. **DTO (Data Transfer Object)** ⭐
**Python status:** Zeer populair!

```python
# Pydantic (modern Python)
from pydantic import BaseModel

class UserDTO(BaseModel):
    id: int
    name: str
    email: str

# Dataclasses (Python 3.7+)
from dataclasses import dataclass

@dataclass
class ProductDTO:
    id: int
    name: str
    price: float
```

### 39. **Unit of Work** 📚
**Python status:** Ingebouwd in SQLAlchemy

```python
from sqlalchemy.orm import Session

with Session() as session:  # Unit of Work
    user = User(name="Jan")
    session.add(user)
    session.commit()  # Atomic transaction
```

### 40. **Identity Map** 📚
**Python status:** SQLAlchemy implementeert dit automatisch

### 41. **Lazy Load** 🐍⭐
**Python status:** Built-in met properties en decorators!

```python
@property
def data(self):
    if not hasattr(self, '_data'):
        self._data = expensive_operation()
    return self._data

# Of met functools
from functools import cached_property

class DataLoader:
    @cached_property
    def data(self):
        return expensive_operation()
```

---

## Python-Specifieke Patterns

### **Context Manager** 🐍
Python's eigen pattern met `with` statement!

```python
with open('file.txt') as f:  # Auto cleanup
    data = f.read()

# Custom context manager
from contextlib import contextmanager

@contextmanager
def database_connection():
    conn = connect()
    try:
        yield conn
    finally:
        conn.close()
```

### **Descriptor Protocol** 🐍
Python's manier voor attribute access control.

```python
class Validator:
    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError("Must be int")
        obj.__dict__[self.name] = value
```

### **Protocol (Structural Subtyping)** 🐍
Python 3.8+ typing feature.

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

# Duck typing met type checking!
```

---

## Samenvatting: Python en Design Patterns

### ✅ **Ingebouwd in Python:**
1. **Iterator** - `__iter__`, `__next__`, generators
2. **Decorator** - `@decorator` syntax
3. **Context Manager** - `with` statement
4. **Prototype** - `copy` module
5. **Flyweight** - String interning, integer caching
6. **Lazy Load** - `@property`, `@cached_property`
7. **Concurrency** - `threading`, `multiprocessing`, `asyncio`

### 🌟 **Meest gebruikt in Python:**
1. **Decorator** - Overal!
2. **Iterator** - Core van Python
3. **Factory** - Frameworks gebruiken dit
4. **Observer** - Event systems, signals
5. **Strategy** - First-class functions maken dit natuurlijk
6. **Adapter** - Duck typing maakt dit makkelijk
7. **Repository** - ORM patterns
8. **DTO** - Pydantic, dataclasses

### 🔧 **Python heeft betere alternatieven:**
1. **Singleton** → Modules, functools
2. **Builder** → Keyword args, dataclasses
3. **Null Object** → Explicit `None`, `or` operator
4. **Strategy** → First-class functions
5. **Service Locator** → Dependency Injection

### 📚 **Framework-specifiek:**
- **Django**: Factory, Template Method, Observer, Repository, MVC
- **Flask**: Decorator, Factory, Chain of Responsibility
- **FastAPI**: Dependency Injection, DTO (Pydantic)
- **SQLAlchemy**: Repository, Unit of Work, Identity Map

---

## Belangrijkste Lessen

1. **Python is pragmatisch**: Veel patterns zijn overbodig door Python features
2. **Duck typing**: Interfaces zijn impliciete, geen expliciete patterns nodig
3. **First-class functions**: Strategy en Command patterns zijn vaak gewoon functies
4. **Built-in protocols**: Iterator, Context Manager zijn deel van de taal
5. **"Pythonic"**: Simpele oplossingen hebben voorkeur boven complexe patterns

**Regel van Thumb:**
> "In Python, als een design pattern meer dan 5 regels code nodig heeft, is er waarschijnlijk een eenvoudiger Pythonic alternatief!"