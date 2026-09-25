# ============================================================
# 3. SET COMPREHENSION
# ============================================================

# Create a set containing only even numbers from 0 to 9
# A set automatically removes duplicate values
evens = {x for x in range(10) if x % 2 == 0}

print(evens)
# Output: {0, 2, 4, 6, 8}

# ===========================================================

"""
3. What is Set Comprehension?

Answer:

Set comprehension is a concise way to create a new set from an iterable, 
optionally applying a condition or transformation.

Eg: Imagine you have numbers from 0–9 and only want unique even numbers. Think: 
    “I need unique values and don't care about duplicates.”

"""

# ==========================================================