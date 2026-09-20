# Odd or Even

## 📌 Problem Statement

Given an integer, determine whether it is **Odd** or **Even**.

**Example:**
```
Input:  19
Output: Odd

Input:  10
Output: Even
```

---

## 🔍 Methods to Solve

### Method 1: Using `if-else` Condition

The simplest way is to use the modulo operator (`%`). If a number is divisible by 2 (remainder is 0), it is Even; otherwise, it is Odd.

**Code:** [01_Odd-or-Even.py](01_Odd-or-Even.py)
```python
n = int(input("Enter the number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Output:**
```
Odd
```

**Execution Flow:**
```
n = 19
   ↓
19 % 2
   ↓
remainder = 1
   ↓
1 == 0 ?
   ↓
False
   ↓
else
   ↓
"Odd"
```

---

### Method 2: Using Ternary / Conditional Operator

Python allows a one-line conditional expression, which is shorter and more concise.

**Code:** [02_Odd-or-Even.py](02_Odd-or-Even.py)
```python
n = 19
print("Even" if n % 2 == 0 else "Odd")
```

**Output:**
```
Odd
```

**Execution Flow:**
```
n = 19
   ↓
n % 2
   ↓
19 % 2 → 1
   ↓
1 == 0 ?
   ↓
False
   ↓
else "Odd"
   ↓
print("Odd")
```

---

### Method 3: Using Bitwise Operator

A number is **Even** if its last bit is `0`, and **Odd** if its last bit is `1`.  
Using the bitwise AND operator `&` with `1` checks only the last bit.

**Code:** [03_Odd-or-Even.py](03_Odd-or-Even.py)
```python
n = 10
print("Even" if n & 1 == 0 else "Odd")
```

**Output:**
```
Even
```

**Execution Flow:**
```
n = 19
   ↓
19 in binary → 10011
   ↓
1 in binary  → 00001
   ↓
10011 & 00001
   ↓
00001 → 1
   ↓
1 == 0 ?
   ↓
False
   ↓
"Odd"
```

---

## ⏱️ Time & Space Complexity

| Method | Time Complexity | Space Complexity |
|--------|-----------------|------------------|
| `if-else` | O(1) | O(1) |
| Ternary Operator | O(1) | O(1) |
| Bitwise Operator | O(1) | O(1) |

---

## 💡 Interview Tips

- **Most common:** The modulo approach (`n % 2 == 0`) is what interviewers usually expect first.
- **Concise version:** The ternary operator shows you know Python shorthand syntax.
- **Bitwise trick:** The bitwise method (`n & 1`) is impressive in interviews because it shows you understand binary operations. It is also slightly faster at the hardware level.
- **Be ready to explain:** Why checking the last bit works — every odd number has its least significant bit set to `1`.
- **Edge cases to mention:** Negative numbers and zero. Zero is Even, and modulo/bitwise still works correctly for negatives in Python.

---

## 🎯 Key Takeaways

1. **`if-else` + `%`** is the standard, beginner-friendly approach.
2. **Ternary operator** is a Pythonic one-liner alternative.
3. **Bitwise `& 1`** is the fastest and most interview-worthy technique.
4. All methods run in **O(1)** time and **O(1)** space.
5. Always verify behavior with **zero** and **negative numbers** in interviews.
