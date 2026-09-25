# Reverse a String

text = input("Enter a string: ")

# Slicing method 
reverse_1 = text[::-1] 
print(reverse_1)


"""
1. Slicing Method

The slicing method reverses the string using a step value of -1. 
It starts from the end of the string and moves backward one character at a time, 
creating a new reversed string. This is the shortest and most Pythonic method.

"""

"""
Execution Flow: 

                Original:  p  y  t  h  o  n
                        ↑              ↓
                        └── -1 step ───┘

                Reversed:  n  o  h  t  y  p
"""