
## 1. What is a Function?

In Python, a function is a modular, reusable block of code that executes to perform a specific task only when it is called.

We use functions for three main reasons:

1. **Reusability:** Write once, run anywhere. It eliminates code redundancy.
2. **Maintainability:** It breaks complex problems into smaller, manageable chunks, making code easier to debug and test.
3. **Readability:** Well-named functions act as documentation, making the codebase cleaner and easier to understand.

Python supports **built-in functions** like `print()` or `len()`, as well as **user-defined functions** created using the `def` keyword. Crucially, functions in Python are **first-class objects**, meaning they can be passed as arguments, returned from other functions, and assigned to variables.

---

## 2. Parameters vs. Arguments

* **Parameter:** A variable defined in the function signature (the variable inside the `def` statement).
* **Argument:** The actual value or object passed to the function when calling it.

```python
def greet(name):       # name = parameter
    print("Hello", name)

greet("Shanmugaraj")   # "Shanmugaraj" = argument

```

---

## 3. What are First-Class Functions?

**Definition:**
A first-class function means that Python treats functions as regular objects—just like integers, strings, or lists. Therefore, a function can be assigned to a variable, passed as an argument, returned from another function, or stored in a data structure.

**Interview Answer:**

 Python supports first-class functions, which means functions are treated as objects. We can assign them to variables, pass them as arguments to other functions, return them from other functions, and store them in data structures. This behavior forms the foundation for advanced concepts like higher-order functions, closures, and decorators.

*`Refer to the full implementation at`* [First-Class_function.py](First-Class_function.py)

---

## 4. What are Higher-Order Functions?

**Interview Answer:**

 A higher-order function is a function that accepts another function as an argument, returns a function, or does both. This is possible because Python treats functions as first-class objects. Higher-order functions are commonly used in functional programming and serve as the foundation for decorators and callbacks.

### 1.1 Function as an Argument

```python
def square(x):
    return x * x

def calculate(func, number):
    # func is another function passed as an argument
    return func(number)

result = calculate(square, 5)
print(result)  # Output: 25

```

**Execution Flow:** `square` → passed to `calculate()` → `calculate(square, 5)` → `func(5)` → **25**

`calculate()` is a higher-order function because it accepts another function (`square`) as an argument.

---

### 1.2 Function Returning a Function

```python
def create_greeting():
    def greet(name):
        return f"Hello, {name}"

    # Return the function object itself, without calling it
    return greet

greeting = create_greeting()
print(greeting("Arun"))  # Output: Hello, Arun

```

**Execution Flow:** `create_greeting()` returns the inner function `greet`, making `create_greeting()` a higher-order function.

