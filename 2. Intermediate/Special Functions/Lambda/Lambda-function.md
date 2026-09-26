# Lambda Function

## 1. What is a Lambda Function?

### Interview Answer

A **lambda function** is a small **anonymous function** in Python defined using the `lambda` keyword. It can accept multiple arguments but contains **only one expression**, whose result is returned automatically.

Lambda functions are mainly used for **short, temporary operations**, especially when a function needs to be passed as an argument to another function.

### Key Idea 
> **Lambda = small function + one expression + inline callback**

---

## 2. Why Are Lambda Functions Used?

Lambda functions are used when:

* The logic is **small and simple**.
* A function is needed **temporarily**.
* A function needs to be passed **inline as an argument**.
* Commonly used with `map()`, `filter()`, and `sorted()`.

### Example

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

**Output:**

```text
[2, 4, 6, 8]
```

Here, `lambda x: x * 2` is passed directly to `map()` as a callback function.

---

## 3. Why Is Lambda Called "Anonymous"?

Lambda functions are called **anonymous** because they can be created **without explicitly giving the function a name**. It can be used directly where it is needed:

```python
sorted(users, key=lambda user: user["age"])
```

> **Note:** A lambda can also be assigned to a variable, but its defining feature is that it is created as a function expression rather than through a named `def` declaration.

---

## 4. Syntax

```python
lambda arguments: expression
```

### Example

```python
square = lambda x: x * x

print(square(5))

# Output 25
```

### How it works

```text
lambda x: x * x
      ↓
    x = 5
      ↓
    5 * 5
      ↓
     25
```

The expression's result is **returned automatically**; a `return` statement is not required.

---

## 5. Lambda vs normal function

| `def`                               | `lambda`                                                   |
| ----------------------------------- | ---------------------------------------------------------- |
| Named function definition           | Anonymous function expression                              |
| Can contain multiple statements     | Contains a single expression                               |
| Suitable for reusable/complex logic | Suitable for short, simple logic                           |
| Can contain loops, `try`, etc.      | Cannot contain statements such as `for`, `while`, or `try` |
| Better for complex functions        | Better for small inline operations                         |
| Supports a function docstring       | Not designed for complex documentation                     |

### Example

**Using `def`:**

```python
def square(x):
    return x * x
```

**Using `lambda`:**

```python
square = lambda x: x * x
```

Both produce the same result:

```python
print(square(5))

# Output 25
```

---

## 6. Common Interview Use Cases

```python
# map()
list(map(lambda x: x * 2, numbers))

# filter()
list(filter(lambda x: x % 2 == 0, numbers))

# sorted()
sorted(users, key=lambda user: user["age"])
```

### Interview Tip

Don't describe lambda simply as **"a shorter way to write `def`."**

A better answer is:

> **Lambda is mainly useful for defining a small function inline, particularly when passing a function as an argument to another function such as `map()`, `filter()`, or `sorted()`.**
