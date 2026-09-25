# Mutable vs Immutable

# Mutable object: list
numbers = [1, 2, 3]

print("Before:", numbers)

numbers.append(4)

print("After:", numbers)


# Immutable object: string
text = "Python"

print("Before:", text)

text = text + " Programming"

print("After:", text)


""" 
Execution flow: 
            Mutable — List:

                        numbers → [1, 2, 3]
                                    ↓
                        numbers.append(4)
                                    ↓
                        same list is changed
                                    ↓
                            [1, 2, 3, 4]

            Immutable — String:

                        text → "Python"
                                ↓
                        text + " Programming"
                                ↓
                        new string is created
                                ↓
                        text → "Python Programming"
"""

""" 
What is Mutable and Immutable data types? 

    Mutable objects are those who values can be changed after creation and the object remains same.
    Eg: List, Set, Dictionary

    Immutable objects cannot be changed after creation. 
    When we try to modify an immutable object., Python creates new object instead of modifying existing one.
    Eg: int, float, str, tuple, bool, and frozenset. 
"""