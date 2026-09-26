# Python Functions — Interview Preparation

---

## 1. What is a Function in Python?

### Interview Answer

A **function** is a reusable block of code that performs a specific task. In Python, a function is defined using the `def` keyword and executed by calling its name. Functions help organize code into smaller, reusable and maintainable units, and they can accept inputs through parameters and optionally return a result using `return`.

### Example

```python
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)

# Output - Hello, Alice!
```

---

## 2. What is the Difference Between a Function Definition and a Function Call?

### Interview Answer

A **function definition** creates the function and specifies what the function should do, while a **function call** executes the function and provides the required arguments. Defining a function does not execute its body; the code inside the function runs only when the function is called.

### Difference

| Function Definition                       | Function Call             |
| ----------------------------------------- | ------------------------- |
| Creates the function                      | Executes the function     |
| Uses `def`                                | Uses the function name    |
| Defines parameters                        | Provides arguments        |
| Function body is not executed immediately | Function body is executed |
| Example: `def add(a, b):`                 | Example: `add(10, 20)`    |

### Example

```python
def add(a, b):          # Function definition
    return a + b

result = add(10, 20)   # Function call
print(result)

# Output - 30
```

---

## 3. What is Variable Scope Inside a Function?

### Interview Answer

**Variable scope** determines where a variable can be accessed in a Python program. A variable created inside a function normally has **local scope**, which means it can be accessed only inside that function. A variable created outside the function can have a wider scope and may be accessed from inside the function according to Python's name-resolution rules.

### Example

```python
def calculate():
    price = 100
    print(price)

calculate()

# Output - 100
```

Here, `price` is a **local variable** because it is created inside `calculate()`.

---

## 4. What are Built-in Functions in Python?

### Interview Answer

**Built-in functions** are functions that Python provides by default, so we can use them without defining them ourselves or importing a module. They perform common operations such as calculating length, converting types, displaying output, and working with collections.

### Example

```python
name = "Python"

print(len(name))
print(type(name))
```

**Output:**

```text
6
<class 'str'>
```

Here, `len()` and `type()` are built-in functions.

---

## 5. What are User-Defined Functions?

### Interview Answer

A **user-defined function** is a function created by the programmer using the `def` keyword to perform a specific task. Unlike built-in functions, its behavior is defined by the developer according to the application's requirements.

### Example

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(500, 3)
print(total)

# Output - 1500
```

---

## 6. What are Pure and Impure Functions?

### Interview Answer

A **pure function** always produces the same output for the same input and does not modify or depend on external state. An **impure function** may depend on or modify something outside the function, so its result or behavior can change based on external state. Pure functions are easier to test and reason about, while impure functions are commonly used when a function needs to interact with external data or state.

### Difference

| Pure Function                       | Impure Function                      |
| ----------------------------------- | ------------------------------------ |
| Same input produces the same output | Output can depend on external state  |
| Does not modify external state      | May modify external state            |
| No side effects                     | Can have side effects                |
| Easier to test                      | Can be harder to test                |
| Example: mathematical calculation   | Example: modifying a global variable |

### Example

```python
# Pure function
def add(a, b):
    return a + b

print(add(10, 20))
print(add(10, 20))
```

**Output:**

```text
30
30
```

The same inputs always produce the same result.

---

## 7. What are Subroutines or Void Functions in Python?

### Interview Answer

A **subroutine** is a function designed to perform an action rather than return a useful result to the caller. Python does not have a separate `void` keyword like some other languages. When a function has no `return` statement, Python automatically returns `None`.

### Example

```python
def display_message():
    print("Welcome to Python")

result = display_message()
print(result)

# Output - Welcome to Python
```

The function performs the action of displaying the message, but it does not return a value.

---

## 8. What is the Difference Between `return`, `yield`, and `print()`?

### Interview Answer

`return` sends a value back to the caller and normally terminates the function. `yield` produces a value from a generator function while pausing its execution so it can continue later. `print()` only displays a value on the screen; it does not send that value back to the caller.

### Difference

| `return`                            | `yield`                                 | `print()`                                   |
| ----------------------------------- | --------------------------------------- | ------------------------------------------- |
| Sends a value to the caller         | Produces values from a generator        | Displays a value                            |
| Terminates the function             | Pauses the function                     | Does not control function execution         |
| Function normally returns once      | Can produce multiple values             | Only outputs text/value                     |
| Caller can store the returned value | Caller can iterate over produced values | Cannot be used to receive the printed value |
| Returns the specified value         | Creates/works with a generator          | Returns `None`                              |

### Example

```python
# return
def get_number():
    return 10

result = get_number()
print(result)

# yield
def generate_numbers():
    yield 10
    yield 20

for number in generate_numbers():
    print(number)

# print
def display_number():
    print(10)

result = display_number()
print(result)
```

**Output:**

```text
10
10
20
10
None
```

---

## 9. What is the LEGB Rule in Python?

### Interview Answer

The **LEGB rule** defines the order Python follows when looking for a variable or function name. Python searches in this order: **Local → Enclosing → Global → Built-in**. It first checks the current function, then any enclosing function, then the global scope, and finally Python's built-in names.

### LEGB Order

| Scope             | Meaning                             |
| ----------------- | ----------------------------------- |
| **L — Local**     | Inside the current function         |
| **E — Enclosing** | Inside an outer function            |
| **G — Global**    | Defined at the module/program level |
| **B — Built-in**  | Names provided by Python            |

### Example

```python
name = "Global"

def outer():
    name = "Enclosing"

    def inner():
        name = "Local"
        print(name)

    inner()

outer()

# Output - Local
```

Python finds `name` in the **Local** scope first, so it does not continue searching.

---

## 10. What is the Difference Between `global` and `nonlocal`?

### Interview Answer

The `global` keyword is used inside a function when we want to modify a variable that belongs to the **global scope**. The `nonlocal` keyword is used inside a nested function when we want to modify a variable belonging to an **enclosing function's scope**.

### Difference

| `global`                              | `nonlocal`                              |
| ------------------------------------- | --------------------------------------- |
| Refers to the global scope            | Refers to an enclosing function's scope |
| Used to modify a global variable      | Used to modify an enclosing variable    |
| Can be used in a normal function      | Used in nested functions                |
| Searches for the name in global scope | Searches in enclosing function scope    |

### Example

```python
count = 10

def update_global():
    global count
    count = 20

update_global()
print(count)

# Output - 20
```

Here, `global count` allows the function to modify the global variable.

### `nonlocal` Example

```python
def outer():
    count = 10

    def inner():
        nonlocal count
        count = 20

    inner()
    print(count)

outer()

# Output - 20
```

Here, `nonlocal count` modifies the variable belonging to `outer()`.

---

## 11. What is a Lambda Function in Python?

### Interview Answer

A **lambda function** is a small anonymous function defined using the `lambda` keyword. It can accept multiple arguments but contains only **one expression**, whose result is returned automatically. Lambda functions are mainly useful for short operations where creating a separate named function would be unnecessary.

### Example

```python
square = lambda x: x * x

print(square(5))

# Output - 25
```

---

## 12. What is a Function Object in Python?

### Interview Answer

In Python, a function is an **object**, which means it can be assigned to a variable, passed as an argument to another function, returned from a function, and stored in a data structure. This is possible because functions are treated as first-class objects in Python.

### Example

```python
def greet():
    return "Hello"

message = greet

print(message())

# Output - Hello
```

Here, `message` refers to the same function object as `greet`.

---

## 13. What are Callback Functions?

### Interview Answer

A **callback function** is a function that is passed to another function as an argument so that the receiving function can call it at the appropriate time. This allows one function to provide behavior that another function can execute.

### Example

```python
def greet(name):
    print(f"Hello, {name}")

def process_user(name, callback):
    callback(name)

process_user("Alice", greet)

# Output - Hello, Alice
```

Here, `greet` is passed to `process_user()` and is called inside it, so `greet` acts as a callback function.

---

## 14. What is a Nested Function in Python?

### Interview Answer

A **nested function** is a function defined inside another function. The inner function can access variables from the outer function's scope. Nested functions are useful when a helper function is needed only within a particular outer function.

### Example

```python
def outer():
    message = "Hello"

    def inner():
        print(message)

    inner()

outer()

# Output - Hello
```

Here, `inner()` is a nested function inside `outer()`, and it can access `message` from the enclosing function.

---

## 15. What are `*args` and `**kwargs` in Python?

### Interview Answer

`*args` allows a function to accept a **variable number of positional arguments** and stores them as a **tuple**. `**kwargs` allows a function to accept a **variable number of keyword arguments** and stores them as a **dictionary**. They are useful when a function needs to accept flexible or unknown numbers of arguments.

### Difference

| `*args`                               | `**kwargs`                            |
| ------------------------------------- | ------------------------------------- |
| Accepts variable positional arguments | Accepts variable keyword arguments    |
| Stores arguments as a tuple           | Stores arguments as a dictionary      |
| Arguments are passed by position      | Arguments are passed using names      |
| Example: `func(10, 20, 30)`           | Example: `func(name="Alice", age=22)` |

