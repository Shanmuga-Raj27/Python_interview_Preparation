# Remove Duplicates from List

# 1. Using set() operation
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))

print(unique)


"""
1. Using `set()`

The `set()` method automatically keeps only unique values, so duplicate elements are removed. 
Converting the set back to a list gives the result as a list. 
However, this method does not guarantee the original order.

"""