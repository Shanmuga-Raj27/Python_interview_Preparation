# sorted() vs sort()

# Function:
# A function can be called independently, without belonging to a specific object.

# Method:
# A method is a function associated with an object/class
# and is called using that object.

"""
sorted():
         - Built-in function
         - Works with different iterables such as list, tuple, and string
         - Returns a NEW sorted list
         - Does NOT modify the original iterable
"""

""" 
sort():
         - List method
         - Works only with lists
         - Modifies the original list in place
         - Returns None

"""

num = [1, 4, 3, 5, 2]

print(num)           # Original list

print(sorted(num))   # Returns a new sorted list

print(num)           # Original list is unchanged

num.sort()           # Sorts the original list

print(num)           # Original list is now sorted


""" 
Execution flow:
                num = [1, 4, 3, 5, 2]
                        ↓
                print(num)
                        ↓
                [1, 4, 3, 5, 2]

                sorted(num)
                        ↓
                NEW sorted list
                        ↓
                [1, 2, 3, 4, 5]
                        ↓
                Original num remains unchanged
                        ↓
                [1, 4, 3, 5, 2]

                num.sort()
                        ↓
                Original num is modified
                        ↓
                [1, 2, 3, 4, 5]
"""