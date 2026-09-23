
# Find prime number using for loop

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


""" 
Explanation: 

    First, num < 2 checks whether the number can be prime. Then the for loop checks every number from 2 up to num - 1. 
    The % operator finds the remainder. If num % i == 0, the number is exactly divisible by i, so it has another factor 
    and is not prime. break immediately stops the loop.
"""

""" 
Execution Flow:
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
"""
