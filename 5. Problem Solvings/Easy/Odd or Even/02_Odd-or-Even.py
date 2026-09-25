# Odd or Even using Ternary / Conditional Operator

n = 19

print("Even" if n%2 == 0 else "Odd")


""" 
Execution Flow: 
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
"""