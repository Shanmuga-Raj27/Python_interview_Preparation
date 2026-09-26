
# Remove Duplicate Elements from a List using Membership operator (in, not in)

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)


# ---------------------------------------------------------------------------------------------------------------------

""" 
Interview Answer:
        Membership operators in and not in are used to test whether a value exists in a sequence or collection. 
        in returns True if the value is present, while not in returns True if the value is absent. 
        They are commonly used for validation, searching, filtering, and access-control checks.
"""

"""
Execution Flow:
                numbers = [10, 20, 10, 30, 20, 40, 30]
                        ↓
                Create empty list: unique_numbers = []
                        ↓
                Take each number one by one
                        ↓
                Check: number not in unique_numbers?
                        ↓
                Yes → Add number
                No  → Skip number
                        ↓
                10 → Add → [10]
                20 → Add → [10, 20]
                10 → Skip
                30 → Add → [10, 20, 30]
                20 → Skip
                40 → Add → [10, 20, 30, 40]
                30 → Skip
                        ↓
                Final Output:
                [10, 20, 30, 40]
"""