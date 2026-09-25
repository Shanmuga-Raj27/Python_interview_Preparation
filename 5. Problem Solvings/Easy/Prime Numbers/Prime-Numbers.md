# Prime Numbers

## 📌 Problem Statement

Given an integer, determine whether it is a **Prime Number** or **Not Prime**.

**Example:**
```
Input:  19
Output: Prime

Input:  20
Output: Not Prime
```

---

## 📖 What is a Prime Number?

A **Prime Number** is a number greater than 1 that has **no positive divisors other than 1 and itself**.

- Prime numbers have **exactly 2 factors**: 1 and the number itself.
- **1 is NOT a prime number** (it has only 1 factor).
- **2 is the only even prime number**.
- Examples of prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23...

---

## 🔍 Methods to Solve

### Method 1: Using `for` Loop (Check All Numbers)

This method checks every number from `2` to `num - 1`. If any number divides `num` exactly (remainder `0`), it is **Not Prime**. If no divisor is found, it is **Prime**.

**Code:** [01_prime_num.py](01_prime_num.py)
```python
num = 20

if num < 2:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
```

**Output:**
```
Not Prime
```

**Execution Flow:**
```
num = 20
   ↓
20 < 2 ?
   ↓
False
   ↓
range(2, 20)
   ↓
i = 2
   ↓
20 % 2 == 0 ?
   ↓
Yes
   ↓
Not Prime
   ↓
break
```

---

### Method 2: Optimized — Check Up to √n

Instead of checking all numbers up to `num - 1`, this method checks only up to the **square root** of the number. This reduces the number of checks and makes the program more efficient.

**Code:** [02_prime_num.py](02_prime_num.py)
```python
num = 19

if num < 2:
    print("Not Prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
```

**Output:**
```
Prime
```

**Execution Flow:**
```
num = 19
   ↓
19 < 2 ?
   ↓
False
   ↓
19 ** 0.5
   ↓
√19 ≈ 4.35
   ↓
int(4.35) + 1
   ↓
range(2, 5)
   ↓
i = 2 → 19 % 2 = 1 → continue
   ↓
i = 3 → 19 % 3 = 1 → continue
   ↓
i = 4 → 19 % 4 = 3 → continue
   ↓
No divisor found
   ↓
Prime
```

---

## ⏱️ Time & Space Complexity

| Method | Time Complexity | Space Complexity |
|--------|-----------------|------------------|
| Check All Numbers | O(n) | O(1) |
| Check Up to √n | O(√n) | O(1) |

**Note:** The optimized method is significantly faster for large numbers because it reduces the number of iterations from `n` to `√n`.

---

## 💡 Interview Tips

- **Always start with `num < 2`:** Numbers less than 2 are not prime by definition.
- **Explain the optimization:** Checking up to `√n` is a key optimization. Be ready to explain why it works — if `n` has a factor larger than `√n`, it must also have a corresponding factor smaller than `√n`.
- **The `for-else` construct:** Python's `for-else` block runs the `else` part only if the loop completes without hitting `break`. This is a clean way to handle prime checking.
- **Edge cases to mention:** Negative numbers, zero, one, and very large numbers.
- **Be ready to extend:** If asked to print all primes up to `n`, mention the **Sieve of Eratosthenes** algorithm.

---

## 🎯 Key Takeaways

1. A **prime number** has exactly 2 factors: 1 and itself.
2. Always check `num < 2` first — these are not prime.
3. The basic prime check runs from `2` to `num - 1` with **O(n)** time complexity.
4. The optimized check runs from `2` to `√num` with **O(√n)** time complexity.
5. Python's `for-else` is a neat pattern for prime checking — `else` runs only if no `break` occurred.
6. For finding all primes up to `n`, the **Sieve of Eratosthenes** is the most efficient algorithm.
