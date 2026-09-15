# Sum of Digits

## 📌 Problem Statement

Given a number, find the sum of all its digits.

**Example:**
```
Input:  12345
Output: 15
```

---

## 🔍 Methods to Solve

### Method 1: Pythonic Approach — `sum()` + `map()`

The `str(a)` converts the number into a string, `map(int, ...)` converts each digit back to an integer, and `sum()` adds all the digits. This is the shortest and most Pythonic solution.

**Code:** [01_Sum-of-digits.py](01_Sum-of-digits.py)
```python
a = 12345
print(sum(map(int, str(a))))
```

**Output:**
```
15
```

**Execution Flow:**
```
a = 12345
   ↓
str(a)
   ↓
"12345"
   ↓
map(int, ...)
   ↓
1 → 2 → 3 → 4 → 5
   ↓
sum(...)
   ↓
1 + 2 + 3 + 4 + 5
   ↓
15
```

---

### Method 2: `for` Loop Method

The loop takes each digit one by one, converts it to an integer, and adds it to `total`.

**Code:** [02_Sum-of-digits.py](02_Sum-of-digits.py)
```python
a = 12345
total = 0

for digit in str(a):
    total += int(digit)

print(total)
```

**Output:**
```
15
```

**Execution Flow:**
```
a = 12345
total = 0

digit = "1" → total = 0 + 1 → 1
digit = "2" → total = 1 + 2 → 3
digit = "3" → total = 3 + 3 → 6
digit = "4" → total = 6 + 4 → 10
digit = "5" → total = 10 + 5 → 15
```

---

### Method 3: Mathematical Method — `%` and `//`

`% 10` extracts the last digit, while `// 10` removes the last digit. The process repeats until the number becomes 0.

**Code:** [03_Sum-of-digits.py](03_Sum-of-digits.py)
```python
a = 12345
total = 0

while a > 0:
    total += a % 10
    a //= 10

print(total)
```

**Output:**
```
15
```

**Execution Flow:**
```
a = 12345
   ↓
12345 % 10 → 5
12345 // 10 → 1234

1234 % 10 → 4
1234 // 10 → 123

123 % 10 → 3
123 // 10 → 12

12 % 10 → 2
12 // 10 → 1

1 % 10 → 1
1 // 10 → 0
   ↓
5 + 4 + 3 + 2 + 1
   ↓
15
```

---

## ⏱️ Time & Space Complexity

| Method | Time Complexity | Space Complexity |
|--------|-----------------|------------------|
| `sum()` + `map()` | O(n) | O(n) |
| `for` Loop | O(n) | O(n) |
| Mathematical (`%` and `//`) | O(n) | O(1) |

---

## 💡 Interview Tips

- **Most Pythonic:** `sum(map(int, str(a)))` is the shortest and most preferred one-liner.
- **Loop approach:** The `for` loop is easy to explain and shows basic iteration logic.
- **Mathematical method:** Using `%` and `//` is interview-friendly when you want to avoid string conversion. It also has **O(1)** space complexity.
- **Be ready to explain:** Why string conversion is used in the first two methods and how the mathematical method avoids it.
- **Edge cases to mention:** Negative numbers, zero, and very large numbers.

---

## 🎯 Key Takeaways

1. **`sum()` + `map()`** is the most concise and Pythonic way to sum digits.
2. **`for` loop** is simple, readable, and demonstrates iteration understanding.
3. **Mathematical method** (`%` and `//`) is optimal for space efficiency with **O(1)** space complexity.
4. All string-based methods use **O(n)** space due to string conversion.
5. Always clarify the **input type** (integer vs string) in interviews before implementing.
