# Object Reference

---

## What is Object Reference in Python?

In Python, everything is an object — lists, strings, integers, functions, classes, etc. An **object reference** is simply a name (variable) that points to an object stored in memory. When you assign a value to a variable, you are not storing the object itself inside the variable; instead, you are storing a **reference** (a memory address pointer) to that object.

### Why is it used?

- **Memory efficiency**: Multiple variables can refer to the same object without duplicating it.
- **Passing behavior**: Determines whether changes inside a function affect the original object.
- **Identity checks**: Using `is` and `id()` to compare references rather than values.

### How it works?

When you write `x = [1, 2, 3]`, Python creates a list object in memory and `x` holds the reference to it. If you write `y = x`, `y` points to the same object — not a copy. To create a separate object, you need to explicitly copy it (shallow/deep copy).

---

## 1. What is the difference between `is` and `==` in Python?

**Answer:**

`==` compares whether two objects have the same value.  
`is` checks whether two variables refer to the same object in memory.  
`id()` can be used to check an object's unique identity.

**Code:**

```python
x = [1, 2, 3]  # Creates a new list object
y = [1, 2, 3]  # Creates another separate list object

z = x           # z does NOT create a new list, z points to the same object as x

print(x is y)      # False → x and y are different objects, Even though their values are the same
print(x == y)      # True → the values inside x and y are the same

print(z is x)     # True → z and x point to the SAME object
print(z == x)      # True → obviously, they have the same values

print(id(x))
print(id(y))       # Different ID → different object

print(id(z))      # Same ID as x → same object
```

**Code:** [is_vs_equal.py](is_vs_equal.py)

**Output:**

```
False
True
True
True
<id_x>
<id_y>
<id_z>
```

---

## 2. What is Mutable and Immutable data types?

**Answer:**

Mutable objects are those whose values can be changed after creation and the object remains same.  
Eg: List, Set, Dictionary

Immutable objects cannot be changed after creation. When we try to modify an immutable object, Python creates new object instead of modifying existing one.  
Eg: int, float, str, tuple, bool, and frozenset.

**Code:**

```python
# Mutable vs Immutable

# Mutable object: list
numbers = [1, 2, 3]

print("Before:", numbers)

numbers.append(4)

print("After:", numbers)


# Immutable object: string
text = "Python"

print("Before:", text)

text = text + " Programming"

print("After:", text)
```

**Code:** [Mutable_vs_Immutable.py](Mutable_vs_Immutable.py)

**Output:**

```
Before: [1, 2, 3]
After: [1, 2, 3, 4]
Before: Python
After: Python Programming
```

**Execution Flow:**

```
Mutable — List:

    numbers → [1, 2, 3]
                ↓
    numbers.append(4)
                ↓
    same list is changed
                ↓
        [1, 2, 3, 4]

Immutable — String:

    text → "Python"
            ↓
    text + " Programming"
            ↓
    new string is created
            ↓
    text → "Python Programming"
```

---

## 3. What is the difference between shallow copy and deep copy in Python?

**Answer:**

A shallow copy creates a new outer object but shares nested objects with the original.

A deep copy creates a completely independent copy, including nested objects.  
Python provides `copy.copy()` for shallow copying and `copy.deepcopy()` for deep copying.

**Code:**

```python
import copy

original = {"a": [1, 2, 3]}

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original["a"].append(99)
print("Original:", original)
print("Shallow Copy:", shallow)  # {'a': [1, 2, 3, 99]} — affected by shared inner list
print("Deep Copy:", deep)     # {'a': [1, 2, 3]}      — fully isolated
```

**Code:** [SwallowCopy_vs_DeepCopy.py](SwallowCopy_vs_DeepCopy.py)

**Output:**

```
Original: {'a': [1, 2, 3, 99]}
Shallow Copy: {'a': [1, 2, 3, 99]}
Deep Copy: {'a': [1, 2, 3]}
```

