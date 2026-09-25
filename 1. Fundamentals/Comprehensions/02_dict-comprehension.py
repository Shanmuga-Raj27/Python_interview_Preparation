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