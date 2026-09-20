# Odd or Even using if-else condition

n = int(input("Enter the number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


""" 
Execution Flow: 
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
"""