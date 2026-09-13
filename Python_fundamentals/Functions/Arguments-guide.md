
## 1. What are Arguments?

An argument is the actual value or object passed to a function when it is called. The function's parameter receives that argument and uses it during execution. There are 4 types of arguments: **Positional**, **Keyword**, **Default**, and **Variable-Length** (`*args`, `**kwargs`).

---

## 2. Positional Arguments

**Interview Answer:**
Positional arguments are arguments passed to a function in a specific order, where values are assigned to parameters based on their position or order.

```python
def introduce(name, age):
    return f"{name}, {age}" 

print(introduce("Arun", 22))
# "Arun" → name
# 22     → age

```

---

## 3. Keyword Arguments

**Interview Answer:**
Keyword arguments are arguments passed using parameter names, allowing Python to match values to the correct parameters regardless of their order. Therefore, their position or order does not matter.

```python
def introduce(name, age):
    return f"{name}, {age}"

# 22, "Arun" are Values/Arguments.
# age, name are keyword/parameter names.
print(introduce(age=22, name="Arun"))

```

---

## 4. Default Arguments

**Interview Answer:**
A default argument is a parameter with a predefined value in a function definition. If the caller does not provide an argument/value for that parameter, Python uses the default value.

If a value is provided, it overrides/replaces the default value.

```python
def greet(name, message="Hello"):
    return f"{message}, {name}"

result_1 = greet("Arun")
# Uses default value: message = "Hello"

result_2 = greet("Arun", "Good morning")
# Provided value replaces the default

print(result_1)
print(result_2)

```

**Here:**

* `name` → Regular parameter
* `message` → Parameter with a default argument value
* `"Hello"` → Default value

> **Interview Tip:** In Python terminology, `"Hello"` is technically the default value of the parameter. Calling `greet("Arun")` means no argument was supplied for `message`, so the default value is used.

---

## 5. What are `*args` and `**kwargs` in Python?

**Answer:**

* `*args` — Allows a function to accept a variable number of positional arguments and stores them as a **tuple**.
* `**kwargs` — Allows a function to accept a variable number of keyword arguments and stores them as a **dictionary**.

They are useful when a function needs to accept a flexible or unknown number of arguments.

*`Refer to code at`* - [03_args_vs_kwargs.py](../03_args_vs_kwargs.py)