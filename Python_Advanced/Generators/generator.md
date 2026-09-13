
---

## 1. What are Generators?

A generator is a special Python function that returns an iterator object using the `yield` keyword to produce values one at a time, instead of storing all values in memory. It pauses its execution after each `yield` while preserving its state, and resumes when the next value is requested. Generators are commonly used for large files, database records, and data pipelines because they process data incrementally and avoid storing the entire dataset in memory.

`yield` → iterator → one value at a time → pause/resume → memory efficient.

---

## 2. What is the Difference Between `yield` and `return`?

| `return` | `yield` |
| --- | --- |
| **Ends the function** and returns a value | **Pauses the function** and produces a value |
| Usually returns a **single/complete result** | Produces **values one at a time** |
| Does not preserve the function's execution state | **Preserves the function's state** so it can resume later |
| Used in normal functions | Used to create a **generator** |
| The returned result may require storing all data in memory | Useful for **memory-efficient** processing of large data |
| Calling the function executes it normally | Calling the function returns a **generator object**; execution happens when values are requested |

---



> **Definition:** `return` terminates a function and return result, whereas `yield` pauses a function, produces a value, preserves its state, and allows it to resume later. `yield` is used to create generators, which produce values one at a time and are useful for memory-efficient processing.

---

## 3. What is the Difference Between Generators and Decorators?

* **Generator:** Controls how values are produced. It uses `yield` and produces values one at a time.
* **Decorator:** Controls how a function behaves. It wraps or modifies a function without changing its original code. It is commonly written using `@`.




| Generator | Decorator |
| --- | --- |
| A generator is a function that produces values one at a time, mainly for memory-efficient data processing. | A decorator is a wrapper that takes another function as input and adds or modifies its behavior without changing its original code. |

---