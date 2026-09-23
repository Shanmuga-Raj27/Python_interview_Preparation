
# Find Factorial of given number using for loop

num = 5
result = 1
for i in range(1, num+1):
    result = result * i

print(f"Factorial of {num} is {result}")


""" 
How it works:
            result starts at 1 because multiplication needs an initial value of 1. The loop goes from 1 to num, 
            and result = result * i multiplies the current result by each number.
"""

""" 
Execution flow:
                num = 5
                result = 1
                    ↓
                i = 1 → 1 × 1  → 1
                    ↓
                i = 2 → 1 × 2  → 2
                    ↓
                i = 3 → 2 × 3  → 6
                    ↓
                i = 4 → 6 × 4  → 24
                    ↓
                i = 5 → 24 × 5 → 120
                    ↓
                print(result)
                    ↓
                120
"""