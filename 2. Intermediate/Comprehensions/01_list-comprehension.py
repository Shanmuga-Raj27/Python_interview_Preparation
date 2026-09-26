# ============================================================
# 1. LIST COMPREHENSION
# ============================================================

# Create a list containing squares of even numbers from 0 to 5
squares = [x ** 2 for x in range(6) if x % 2 == 0]

print(squares)
# Output: [0, 4, 16]


""" 

Q: What is comprehension in Python?

Answer:

 Comprehension is a concise way to create a new collection
 from an iterable, with optional filtering or transformation.
 Python supports list, dictionary, and set comprehensions.


LIST       → I want a collection of values
             [0, 4, 16]

DICTIONARY → I want KEY → VALUE relationships
             {"apple": 5, "kiwi": 4}

SET        → I want UNIQUE values
             {0, 2, 4, 6, 8}

"""

# =======================================================================================

"""
1. What is List Comprehension?

Answer:

List comprehension is a concise way to create a new list from an iterable, 
optionally applying a condition or transformation.

Eg: Imagine you have numbers from 0–5 and want a list of squares of only even numbers. 
    Think: “I need an ordered collection of values.”

"""