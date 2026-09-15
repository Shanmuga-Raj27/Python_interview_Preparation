# Swap two variables

# 1. The Pythonic method: Tuple Unpacking
a = 10
b = 20

a, b = b, a

print(a, b)


"""
1. Pythonic Method — Tuple Unpacking

Python allows multiple variables to be assigned at the same time. 
Here, the value of `b` is assigned to `a`, and the original value of `a` is assigned to `b` in a single statement. 
No temporary variable is required.

"""