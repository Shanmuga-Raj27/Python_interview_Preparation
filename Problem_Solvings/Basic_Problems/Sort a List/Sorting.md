# Sort a List

## 📌 Problem Statement

Given a list of numbers, sort it in **ascending** or **descending** order.

**Example:**
```
Input:  [1, 2, 4, 7, 3, 5]
Output: [1, 2, 3, 4, 5, 7]  (Ascending)
Output: [7, 5, 4, 3, 2, 1]  (Descending)
```

---

## 🔍 Methods to Solve

### Method 1: Using `sorted()` Function

`sorted()` is a built-in Python function that works with any iterable (list, tuple, string, etc.) and returns a **new sorted list** without modifying the original.

**Ascending Order:**
**Code:** [sort-list.py](sort-list.py)
```python
num = [1, 2, 4, 7, 3, 5]
print(sorted(num))
```

**Output:**
```
[1, 2, 3, 4, 5, 7]
```

**Descending Order:**
```python
print(sorted(num, reverse=True))
```

**Output:**
```
[7, 5, 4, 3, 2, 1]
```

**Execution Flow:**
```
num = [1, 2, 4, 7, 3, 5]
      ↓
sorted(num)
      ↓
Returns new sorted list → [1, 2, 3, 4, 5, 7]
Original num remains → [1, 2, 4, 7, 3, 5]
```

---

### Method 2: Using `list.sort()` Method

`sort()` is a **list method** that sorts the list **in place** (modifies the original list) and returns `None`. It works only with lists.

**Code:** [Sorted-vs-Sort.py](Sorted-vs-Sort.py)
```python
num = [1, 4, 3, 5, 2]

print(num)       # Original list

print(sorted(num))   # Returns new sorted list

print(num)       # Original list is unchanged

num.sort()       # Sorts the original list

print(num)       # Original list is now sorted
```

**Output:**
```
[1, 4, 3, 5, 2]   # Original
[1, 2, 3, 4, 5]   # sorted() result
[1, 4, 3, 5, 2]   # Original unchanged
[1, 2, 3, 4, 5]   # After num.sort()
```

**Execution Flow:**
```
num = [1, 4, 3, 5, 2]
      ↓
print(num)
      ↓
[1, 4, 3, 5, 2]

sorted(num)
      ↓
NEW sorted list
      ↓
[1, 2, 3, 4, 5]
Original num remains unchanged
      ↓
[1, 4, 3, 5, 2]

num.sort()
      ↓
Original num is modified
      ↓
[1, 2, 3, 4, 5]
```

---

## 📊 `sorted()` vs `sort()` Comparison

| Feature | `sorted()` | `sort()` |
|---------|-----------|----------|
| Type | Built-in function | List method |
| Works with | Any iterable (list, tuple, string, etc.) | Lists only |
| Return value | New sorted list | `None` (modifies in place) |
| Modifies original? | ❌ No | ✅ Yes |
| Syntax | `sorted(iterable)` | `list.sort()` |

---

## ⏱️ Time & Space Complexity

| Method | Time Complexity | Space Complexity |
|--------|-----------------|------------------|
| `sorted()` | O(n log n) | O(n) |
| `sort()` | O(n log n) | O(1) / O(log n) |

**Note:** Both use TimSort algorithm internally (Python's default sorting algorithm).

---

## 💡 Interview Tips

- **Most asked:** The difference between `sorted()` and `sort()` is a very common interview question.
- **When to use `sorted()`:** When you need to keep the original list unchanged or when working with non-list iterables like tuples or strings.
- **When to use `sort()`:** When you want to save memory by sorting the list in place.
- **Be ready to explain:** Why `sort()` returns `None` and how in-place sorting saves memory.
- **Key phrase to remember:** `sorted()` returns a new list; `sort()` modifies the existing list.

---

## 🎯 Key Takeaways

1. **`sorted()`** is a function that returns a **new sorted list** and works with any iterable.
2. **`sort()`** is a list method that sorts the list **in place** and returns `None`.
3. Both methods use the **Timsort** algorithm with **O(n log n)** time complexity.
4. `sorted()` uses **O(n)** extra space; `sort()` uses less space because it sorts in place.
5. If you write `print(num.sort())`, it will print `None` — not the sorted list. This is a common mistake.
