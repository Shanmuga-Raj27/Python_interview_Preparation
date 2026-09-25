# Odd or Even using Bitwise Operator

n = 10

print("Even" if n & 1 == 0 else "Odd")


""" 
Execution Flow: 
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
"""