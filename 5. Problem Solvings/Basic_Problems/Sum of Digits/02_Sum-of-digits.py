# Sum of Digits

# 2. for Loop Method

a = 12345
total = 0

for digit in str(a):
    total += int(digit)

print(total)


""" 
How it works: The loop takes each digit one by one, converts it to an integer, and adds it to total.

Execution flow:
                a = 12345
                total = 0

                digit = "1" → total = 0 + 1 → 1
                digit = "2" → total = 1 + 2 → 3
                digit = "3" → total = 3 + 3 → 6
                digit = "4" → total = 6 + 4 → 10
                digit = "5" → total = 10 + 5 → 15

"""