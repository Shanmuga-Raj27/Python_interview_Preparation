
# Find prime number - check up to √n optimization

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


""" 
Explanation:

        This method uses the same basic idea, but instead of checking all numbers up to num - 1, 
        it checks only up to the square root of the number. num ** 0.5 calculates the square root, 
        and int() converts it to an integer. This reduces the number of checks and makes the program more efficient.
"""

""" 
Execution Flow: 
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
"""



