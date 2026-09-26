
# Normal division: always returns float

print(10 / 3)    # 3.3333333333333335

print(10 / 2)    # 5.0
                 # Whole-number result, but still a float


# Floor division: rounds down toward negative infinity

print(10 // 3)   # 3

print(10 // 2)   # 5

print(7.5 // 2)  # 3.0
                 # Float input -> float result, after flooring


# The important case: negative numbers

print(-10 / 3)   # -3.3333333333333335

print(-10 // 3)  # -4
                 # Rounds down toward -infinity, NOT toward zero

print(10 // -3)  # -4
                 # Same floor-division rule


# Modulus: returns the remainder

print(10 % 3)    # 1

print(10 % 2)    # 0
                 # 0 means the number is exactly divisible

# -------------------------------------------------------------------------------------------------------------------------                 

""" 
What is the difference between / and // in Python?

Interview Answer:

    / is the normal division operator:

        It always returns the result as a float, even when both operands are integers and 
        the result is a whole number.

    // is the floor division operator:

        It divides two numbers and returns the largest value that is less than or equal to the actual result, 
        meaning it rounds down toward negative infinity. When both operands are integers, the result is usually an int; 
        when at least one operand is a float, the result is a float.

    % is the modulus (remainder) operator:

        It returns the remainder left after division and is commonly used to check divisibility.

"""
