# ============================================================
# 1. LIST COMPREHENSION
# ============================================================

# Create a list containing squares of even numbers from 0 to 5
squares = [x ** 2 for x in range(6) if x % 2 == 0]

print(squares)
# Output: [0, 4, 16]


# ============================================================
# 2. DICTIONARY COMPREHENSION
# ============================================================

# Create a dictionary where each word is the key
# and the length of the word is the value
word_lengths = {
    word: len(word)
    for word in ["apple", "kiwi", "banana"]
}

print(word_lengths)
# Output: {'apple': 5, 'kiwi': 4, 'banana': 6}


# ============================================================
# 3. SET COMPREHENSION
# ============================================================

# Create a set containing only even numbers from 0 to 9
# A set automatically removes duplicate values
evens = {x for x in range(10) if x % 2 == 0}

print(evens)
# Output: {0, 2, 4, 6, 8}


# ============================================================
# INTERVIEW Q/A
# ============================================================

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

# ===========================================================

"""
2. What is Dictionary Comprehension?

Answer:

Dictionary comprehension is a concise way to create a new dictionary from an iterable using key-value expressions, 
optionally with a condition.

Eg: Imagine you have words and want to store each word as a key and its length as the value. 
    Think: “I need a key → value relationship.”

"""

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