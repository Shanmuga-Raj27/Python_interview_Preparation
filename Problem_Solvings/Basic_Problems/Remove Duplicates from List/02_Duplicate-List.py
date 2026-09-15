# Remove Duplicates from List

numbers = [1, 2, 2, 3, 4, 4, 5]

# Using a for loop — preserves order

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)

"""
2. Using a `for` Loop

The `for` loop checks each element one by one and adds it to a new list only if it is not already present. 
This removes duplicates while preserving the original order of the elements.

"""

""" 
Execution Flow: 
                numbers → [1, 2, 2, 3, 4, 4, 5]
                            ↓
                unique → []

                1 → not in unique → add → [1]
                2 → not in unique → add → [1, 2]
                2 → already exists → skip
                3 → not in unique → add → [1, 2, 3]
                4 → not in unique → add → [1, 2, 3, 4]
                4 → already exists → skip
                5 → not in unique → add → [1, 2, 3, 4, 5]
                            ↓
                        print()
                            ↓
                    [1, 2, 3, 4, 5]
"""