# Reverse a String

## 📌 Problem Statement

Given a string, reverse the order of its characters and return the reversed string.

**Example:**
```
Input:  python
Output: nohtyp
```

---

## 🔍 Methods to Solve

### Method 1: Slicing Method

The slicing method reverses the string using a step value of -1. It starts from the end of the string and moves backward one character at a time, creating a new reversed string. This is the shortest and most Pythonic method.

**Code:** [01_Reverse-String.py](01_Reverse-String.py)
```python
text = input("Enter a string: ")
reverse_1 = text[::-1]
print(reverse_1)
```

**Output:**
```
nohtyp
```

**Execution Flow:**
```
Original:  p  y  t  h  o  n
        ↑              ↓
        └── -1 step ───┘

Reversed:  n  o  h  t  y  p
```

---

### Method 2: `reversed()` Function Method

The `reversed()` function reads the string characters from last to first and returns them as a reverse iterator. The `join()` method then combines those characters into a single string. This method is also simple and commonly accepted in interviews.

**Code:** [02_Reverse-String.py](02_Reverse-String.py)
```python
text = input("Enter a string: ")
reverse_2 = "".join(reversed(text))
print(reverse_2)
```

**Output:**
```
nohtyp
```

**Execution Flow:**
```
text = "python"
     ↓
reversed(text)
     ↓
"n" → "o" → "h" → "t" → "y" → "p"
     ↓
"".join(...)          # join() combines characters
     ↓
"nohtyp"
     ↓
print(reverse_2)
     ↓
nohtyp
```

---

### Method 3: `for` Loop Method

The `for` loop goes through each character in the original string. Each character is added before the characters already stored, so the string gradually builds in reverse order. This method is useful in interviews because it demonstrates your understanding of loops and string manipulation.

**Code:** [03_Reverse-String.py](03_Reverse-String.py)
```python
text = input("Enter a string: ")
reverse_3 = ""

for char in text:
    reverse_3 = char + reverse_3

print(reverse_3)
```

**Output:**
```
nohtyp
```

**Execution Flow:**
```
text = "python"
reverse_3 = ""
      ↓
char = "p"
reverse_3 = "p" + "" → "p"
      ↓
char = "y"
reverse_3 = "y" + "p" → "yp"
      ↓
char = "t"
reverse_3 = "t" + "yp" → "typ"
      ↓
char = "h"
reverse_3 = "h" + "typ" → "htyp"
      ↓
char = "o"
reverse_3 = "o" + "htyp" → "ohtyp"
      ↓
char = "n"
reverse_3 = "n" + "ohtyp" → "nohtyp"
      ↓
print(reverse_3)
      ↓
"nohtyp"
```

---

## ⏱️ Time & Space Complexity

| Method | Time Complexity | Space Complexity |
|--------|-----------------|------------------|
| Slicing | O(n) | O(n) |
| `reversed()` + `join()` | O(n) | O(n) |
| `for` Loop | O(n) | O(n) |

---

## 💡 Interview Tips

- **Most Pythonic:** Slicing (`[::-1]`) is the shortest and most preferred method in Python.
- **Built-in function:** `reversed()` + `join()` shows you know Python built-ins.
- **Loop approach:** The `for` loop method is often asked in interviews to test your understanding of string manipulation and loop logic.
- **Be ready to explain:** Why string concatenation inside a loop (`char + reverse_3`) works and how it builds the reversed string.
- **Edge cases to mention:** Empty string, single character, special characters, and Unicode characters.

---

## 🎯 Key Takeaways

1. **Slicing (`[::-1]`)** is the most concise and Pythonic way to reverse a string.
2. **`reversed()` + `join()`** is a clean, readable alternative using built-in functions.
3. **`for` loop** method is interview-friendly and demonstrates loop logic understanding.
4. All methods have **O(n)** time and space complexity since strings are immutable and a new string must be created.
5. Always handle **edge cases** like empty strings when implementing in interviews.
