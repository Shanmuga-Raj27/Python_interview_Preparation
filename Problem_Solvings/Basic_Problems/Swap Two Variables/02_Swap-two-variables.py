# Swap two variables

# 2. The Traditional method: Using a Temporary Variable
a = 10
b = 20

temp = a
a = b
b = temp

print(a, b)


"""
2. Traditional Method — Temporary Variable

First, the value of `a` is stored safely in a Temporary variable. 
Then, `b` is assigned to `a`, and finally the stored value from the Temporary variable is assigned to `b`. 
This swaps the values using an extra variable.

"""