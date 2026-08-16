# Python Interview Questions & Answers

A curated collection of the most commonly asked Python interview topics, organized as
concise Q&A with runnable sample code.

---

## 1. Language Fundamentals

### Q1.1 — What is the difference between `is` and `==`?

`==` checks value equality (calls `__eq__`), while `is` checks identity (same object in memory).

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  — same values
print(a is b)   # False — different objects

# interning: small strings and ints are cached
x = "hello"
y = "hello"
print(x is y)   # True  — same interned object
```

### Q1.2 — Explain *shallow* vs *deep* copy.

```python
import copy

original = {"a": [1, 2, 3]}

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original["a"].append(99)
print(shallow)  # {'a': [1, 2, 3, 99]} — affected by shared inner list
print(deep)     # {'a': [1, 2, 3]}      — fully isolated
```

### Q1.3 — What are Python's built-in data structures and their time complexities?

| Structure | Lookup (key/index) | Insert | Notes |
|-----------|---------------------|--------|-------|
| `list`    | O(n) / O(1) append  | O(1) amortized | ordered, mutable, allows duplicates |
| `tuple`   | O(1) / O(n) | immutable | hashable when elements are hashable |
| `dict`    | O(1) average        | O(1) average | insertion-ordered (Py 3.7+), hash table |
| `set`     | O(1) average        | O(1) average | unordered, unique, hash based |
| `deque`   | O(1) both ends      | O(1) | from `collections`, fast queue/stack |

### Q1.4 — What is the `*args` and `**kwargs` syntax?

```python
def func(a, *args, **kwargs):
    print("positional:", a)
    print("extra positional:", args)        # tuple
    print("keyword:", kwargs)               # dict

func(1, 2, 3, 4, name="Alice", age=30)
```

### Q1.5 — What is a list/dict comprehension?

```python
# List comprehension
squares = [x ** 2 for x in range(6) if x % 2 == 0]
# -> [0, 4, 16]

# Dict comprehension
word_lengths = {w: len(w) for w in ["apple", "kiwi", "banana"]}
# -> {'apple': 5, 'kiwi': 4, 'banana': 6}

# Set comprehension
evens = {x for x in range(10) if x % 2 == 0}
```

### Q1.6 — What is the ternary operator?

```python
result = "even" if 4 % 2 == 0 else "odd"
```

---

## 2. Object-Oriented Programming

### Q2.1 — What is the difference between `__init__` and `__new__`?

`__new__` creates (allocates) the instance; `__init__` initializes it. `__new__` runs first and is rarely overridden.

```python
class Demo:
    def __new__(cls, *args, **kwargs):
        print("__new__ — creating instance")
        return super().__new__(cls)

    def __init__(self, value):
        print("__init__ — initializing instance")
        self.value = value

d = Demo(10)
```

### Q2.2 — Explain instance, class, and static methods.

```python
class Calculator:
    factor = 1.1  # class attribute

    def __init__(self, base):
        self.base = base

    def instance_method(self):       # has access to self
        return self.base

    @classmethod
    def class_method(cls):           # has access to cls
        return cls.factor

    @staticmethod
    def static_method(x, y):         # no implicit access
        return x * y

print(Calculator.class_method())
print(Calculator.static_method(2, 3))
```

### Q2.3 — What is `@property` and when to use it?

`@property` lets a method be accessed as an attribute — useful for getters/setters with validation.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("radius must be positive")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
c.radius = 10          # setter validates
print(c.area)          # computed property, no parentheses
```

### Q2.4 — Explain MRO (Method Resolution Order) and the diamond problem.

```python
class A:
    def say(self): print("A")

class B(A):
    def say(self): print("B"); super().say()

class C(A):
    def say(self): print("C"); super().say()

class D(B, C):
    pass

D().say()           # B -> C -> A
print(D.__mro__)    # MRO: D -> B -> C -> A
```

### Q2.5 — What is inheritance vs composition?

```python
# Inheritance — "is-a"
class Animal:
    def speak(self): ...

class Dog(Animal):
    def speak(self): print("Woof")

# Composition — "has-a"
class Engine:
    def start(self): print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()   # Car HAS-A Engine

    def drive(self):
        self.engine.start()
        print("Driving")
```

---

## 3. Decorators, Generators & Iterators

### Q3.1 — What is a decorator?

A decorator is a function that wraps another function, adding behavior.

```python
import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 4)
```

### Q3.2 — What is `functools.wraps` and why use it?

It copies metadata (`__name__`, `__doc__`) from the wrapped function to the wrapper, aiding debugging.

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### Q3.3 — What is the difference between a generator and an iterator?

- **Iterator**: object with `__iter__` and `__next__`; traversed once, raises `StopIteration`.
- **Generator**: a special iterator defined with `yield`; lazily computes values.

```python
# Iterator class
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

for n in Counter(1, 3):
    print(n)

# Generator function
def gen_counter(low, high):
    while low <= high:
        yield low
        low += 1

print(list(gen_counter(1, 4)))
```

### Q3.4 — What is `yield from`?

Delegates to a sub-generator — useful for flattening or composing generators.

```python
def flatten(nested):
    for sub in nested:
        yield from sub

list(flatten([[1, 2], [3, 4]]))  # [1, 2, 3, 4]
```

### Q3.5 — What are generator expressions vs list comprehensions?

```python
# List comprehension — builds the full list in memory
squares_list = [x ** 2 for x in range(1000)]

# Generator expression — yields one at a time (lazy)
squares_gen = (x ** 2 for x in range(1000))
```

---

## 4. Context Managers

### Q4.1 — How does a `with` statement work? Implement a custom context manager.

A context manager implements `__enter__` and `__exit__`.

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False  # don't suppress exceptions

with Timer() as t:
    x = sum(range(1_000_000))
print(f"Result: {x}")
```

### Q4.2 — How to create a context manager with `contextlib`?

```python
from contextlib import contextmanager

@contextmanager
def managed_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()

with managed_file("test.txt", "w") as f:
    f.write("Hello")
```

---

## 5. Concurrency & Parallelism

### Q5.1 — What is the GIL (Global Interpreter Lock)?

The GIL ensures only one thread executes Python bytecodes at a time. This means
**threads are not truly parallel for CPU-bound work**, but they are fine for
**I/O-bound** tasks.

```python
import threading

print("Default threads:", threading.active_count())
# CPU-bound work does NOT benefit from threads due to GIL
```

### Q5.2 — When to use threads vs processes vs async?

```python
# Threading — good for I/O-bound (network, file)
import threading
threads = [threading.Thread(target=download, args=(url,)) for url in urls]

# Multiprocessing — good for CPU-bound (true parallelism)
import multiprocessing
procs = [multiprocessing.Process(target=cpu_task, args=(i,)) for i in range(4)]

# asyncio — good for I/O-bound with many connections (single-thread async)
import asyncio

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch(session, u) for u in urls])
```

### Q5.3 — Explain the `asyncio` event loop with a runnable example.

```python
import asyncio

async def task(name, delay):
    print(f"{name} starting")
    await asyncio.sleep(delay)
    print(f"{name} done after {delay}s")
    return f"{name} result"

async def main():
    # gather runs coroutines concurrently
    results = await asyncio.gather(
        task("A", 1),
        task("B", 2),
    )
    print(results)

asyncio.run(main())
```

### Q5.4 — What is `concurrent.futures`?

A high-level interface for asynchronously executing callables using threads or processes.

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_url(url):
    import requests
    return requests.get(url).status_code

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(fetch_url, url): url for url in urls}
    for future in as_completed(futures):
        print(f"{futures[future]}: {future.result()}")
```

---

## 6. Memory Management & Performance

### Q6.1 — How does Python manage memory?

- **Reference counting**: each object tracks how many references point to it.
- **Cycle detector**: garbage collector (`gc`) catches reference cycles.
- **Memory pools/arenas**: small objects are pooled; large ones go to the system allocator.

```python
import sys
x = 42
print(sys.getrefcount(x))   # number of references to x

import gc
print(gc.get_objects())     # all tracked objects
gc.collect()                # force cycle collection
```

### Q6.2 — What are `__slots__` and why use them?

`__slots__` restricts attribute creation and reduces memory per instance.

```python
class WithSlots:
    __slots__ = ["x", "y"]
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = WithSlots(1, 2)
# obj.z = 3   # AttributeError — no __dict__ created
```

### Q6.3 — How to profile and optimize Python code?

```python
import cProfile, pstats

def slow():
    return sum(i * i for i in range(10_000))

cProfile.run("slow()", "profile_stats")
stats = pstats.Stats("profile_stats")
stats.sort_stats("cumulative").print_stats(10)
```

Tools: `timeit`, `cProfile`, `memory_profiler`, `line_profiler`.

---

## 7. Modules, Packaging & Virtual Environments

### Q7.1 — What is the difference between a module, a package, and a library?

- **Module**: a single `.py` file.
- **Package**: a directory with `__init__.py` (a namespace can be a package without it).
- **Library**: a reusable collection of modules/packages distributed via `pip`.

### Q7.2 — Explain the `if __name__ == "__main__"` pattern.

```python
# math_utils.py
def add(a, b): return a + b

if __name__ == "__main__":
    # Runs only when executed directly, not when imported
    print(add(2, 3))
```

### Q7.3 — What are absolute vs relative imports?

```python
# Absolute (preferred, PEP 8)
from mypackage.module import func

# Relative (discouraged, but valid)
from . import module
from ..subpkg import other
```

### Q7.4 — How to manage dependencies?

```bash
python -m venv .venv                 # create venv
source .venv/bin/activate            # activate (Unix)
.venv\Scripts\activate               # activate (Windows)

pip install -r requirements.txt      # install deps
pip freeze > requirements.txt        # freeze versions
# Modern: use pyproject.toml + pip-tools or poetry/uv
```

---

## 8. Exception Handling

### Q8.1 — How does exception handling work under the hood?

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("No exception occurred")   # runs only if no exception
finally:
    print("Always runs")             # cleanup, always executes

# Raising and re-raising
try:
    risky()
except ValueError:
    print("Handling")
    raise                          # re-raises the same exception
```

### Q8.2 — What is a custom exception?

```python
class MyError(Exception):
    """Base custom error."""
    pass

class ValidationError(MyError):
    def __init__(self, message, field=None):
        super().__init__(message)
        self.field = field

try:
    raise ValidationError("Invalid email", field="email")
except ValidationError as e:
    print(e, e.field)
```

---

## 9. Functional Programming Tools

### Q9.1 — Explain `map`, `filter`, `reduce`.

```python
from functools import reduce

nums = [1, 2, 3, 4]

# map — transform each
doubled = list(map(lambda x: x * 2, nums))   # [2, 4, 6, 8]

# filter — keep matching
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

# reduce — aggregate
total = reduce(lambda a, b: a + b, nums, 0)     # 10
# prefer: sum(nums)
```

---

## 10. Dunder (Magic) Methods

### Q10.1 — Common dunder methods and their purpose.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):          # unambiguous representation
        return f"Vector({self.x}, {self.y})"

    def __str__(self):           # human-readable representation
        return f"({self.x}, {self.y})"

    def __eq__(self, other):     # equality
        if not isinstance(other, Vector): return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):     # ordering (enables sort)
        return (self.x, self.y) < (other.x, other.y)

    def __len__(self):           # len()
        return 2

    def __getitem__(self, i):    # v[0]
        return (self.x, self.y)[i]

    def __add__(self, other):    # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

v = Vector(3, 4)
print(repr(v))    # Vector(3, 4)
print(v == Vector(3, 4))  # True
```

---

## 11. Design Patterns in Python

### Q11.1 — Singleton pattern.

```python
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Alternative: use a metaclass or a decorator
```

### Q11.2 — Factory pattern.

```python
class Dog:
    def speak(self): return "Woof"

class Cat:
    def speak(self): return "Meow"

class AnimalFactory:
    @staticmethod
    def create(animal_type):
        animals = {"dog": Dog, "cat": Cat}
        return animals[animal_type]()

AnimalFactory.create("dog").speak()
```

### Q11.3 — Observer pattern with callbacks.

```python
class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, callback):
        self._observers.append(callback)

    def notify(self, msg):
        for cb in self._observers:
            cb(msg)

s = Subject()
s.subscribe(lambda msg: print(f"Got: {msg}"))
s.notify("hello")
```

---

## 12. Common Interview Code Problems

### Q12.1 — Reverse a linked list in place.

```python
class Node:
    def __init__(self, val=0, nxt=None):
        self.val, self.next = val, nxt

def reverse(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
```

### Q12.2 — Check if a string has all unique characters.

```python
def is_unique(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    return True
```

### Q12.3 — LRU Cache with `functools.lru_cache`.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### Q12.4 — Two-sum.

```python
def two_sum(nums, target):
    index_of = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_of:
            return index_of[complement], i
        index_of[num] = i
    return None, None
```

---

## 13. Best Practices & PEPs

- **PEP 8**: Style guide — 4-space indent, `snake_case` for functions/vars, `CamelCase` for classes.
- **PEP 20 (Zen of Python)**: `import this`.
- **PEP 257**: Docstring conventions.
- Use **type hints**: `def add(a: int, b: int) -> int: ...`
- Prefer **`pathlib.Path`** over `os.path`.
- Always use **`if __name__ == "__main__":`** guard.
- **Never** commit `.env` (secrets) — handled by this `.gitignore`.

```python
import this  # The Zen of Python
```

---

## 14. Frequently Asked Questions

### Q14.1 — Mutable default argument gotcha.

```python
# BAD — the list is shared across calls
def append_to(item, target=[]):
    target.append(item)
    return target

# GOOD
def append_to(item, target=None):
    target = target or []
    target.append(item)
    return target
```

### Q14.2 — What are descriptors?

```python
# property, classmethod, and staticmethod are all implemented as descriptors
class MyDescriptor:
    def __get__(self, obj, owner):
        return getattr(obj, "_value", None)
    def __set__(self, obj, value):
        obj._value = value

class Demo:
    val = MyDescriptor()
    def __init__(self, v):
        self.val = v
```

### Q14.3 — Explain the iterator protocol.

An **iterable** has `__iter__()` (returns an iterator). An **iterator** has `__next__()`
(returning the next item) and `__iter__()` (returns self).

```python
class MyIter:
    def __init__(self, items):
        self._items = list(items)
        self._idx = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._idx >= len(self._items):
            raise StopIteration
        val = self._items[self._idx]
        self._idx += 1
        return val
```
