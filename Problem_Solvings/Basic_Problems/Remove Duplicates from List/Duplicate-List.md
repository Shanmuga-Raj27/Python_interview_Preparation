# Remove Duplicates from List

## 📌 Problem Statement

Given a list containing duplicate elements, remove the duplicates and return a list with only unique values.

**Example:**
```
Input:  [1, 2, 2, 3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]
```

---

## 🔍 Methods to Solve

### Method 1: Using `set()` Operation

The `set()` method automatically keeps only unique values, so duplicate elements are removed. Converting the set back to a list gives the result as a list.

**⚠️ Note:** This method does not guarantee the original order.

**Code:** [01_Duplicate-List.py](01_Duplicate-List.py)
```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print(unique)
```

**Output:**
```
[1, 2, 3, 4, 5]
```

---

### Method 2: Using a `for` Loop (Preserves Order)

The `for` loop checks each element one by one and adds it to a new list only if it is not already present. This removes duplicates while preserving the original order of the elements.

**Code:** [02_Duplicate-List.py](02_Duplicate-List.py)
```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)
```

**Output:**
```
[1, 2, 3, 4, 5]
```

**Execution Flow:**
```
numbers → [1, 2, 2, 3, 4, 4, 5]
              ↓
unique → []

 1 → not in unique → add → [1]
 2 → not in unique → add → [1, 2]
 2 → already exists → skip
 3 → not in unique → add → [1, 2, 3]
 4 → not in unique → add → [1, 2, 3, 4]
 4 → already exists → skip
 5 → not in unique → add → [1, 2, 3, 4, 5]
              ↓
          print()
              ↓
      [1, 2, 3, 4, 5]
```

---

## ⏱️ Time & Space Complexity

| Method | Time Complexity | Space Complexity | Preserves Order |
|--------|-----------------|------------------|-----------------|
| `set()` | O(n) | O(n) | ❌ No |
| `for` Loop | O(n²) | O(n) | ✅ Yes |

---

## 💡 Interview Tips

- **When to use `set()`:** When order doesn't matter and you want a concise, one-line solution.
- **When to use `for` loop:** When you need to preserve the original order of elements.
- **Alternative approaches:** You can also use `dict.fromkeys()` which preserves order and runs in O(n) time (Python 3.7+).
  ```python
  numbers = [1, 2, 2, 3, 4, 4, 5]
  unique = list(dict.fromkeys(numbers))
  print(unique)  # [1, 2, 3, 4, 5]
  ```
- Be prepared to explain **why** one method is chosen over another based on requirements like order preservation and performance.

---

## 🎯 Key Takeaways

1. `set()` is the **simplest** way to remove duplicates but **does not preserve order**.
2. The `for` loop approach is **order-preserving** but has **O(n²)** time complexity.
3. For **order preservation + O(n) time**, use `dict.fromkeys()` in Python 3.7+.
4. Always consider the **requirements** of the problem (order vs performance) before choosing an approach.
