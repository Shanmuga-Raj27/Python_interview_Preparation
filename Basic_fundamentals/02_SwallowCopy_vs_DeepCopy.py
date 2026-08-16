import copy

original = {"a": [1, 2, 3]}

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original["a"].append(99)
print("Original:", original)
print("Shallow Copy:", shallow)  # {'a': [1, 2, 3, 99]} — affected by shared inner list
print("Deep Copy:", deep)     # {'a': [1, 2, 3]}      — fully isolated

"""
Question: What is the difference between shallow copy and deep copy in Python?

Answer:

A shallow copy creates a new outer object but shares nested objects with the original.
A deep copy creates a completely independent copy, including nested objects.
Python provides copy.copy() for shallow copying and copy.deepcopy() for deep copying.
"""