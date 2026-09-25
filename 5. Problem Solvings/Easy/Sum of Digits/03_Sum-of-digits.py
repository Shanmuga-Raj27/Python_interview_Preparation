# Sum of Digits

# 3. Mathematical Method — % and //

a = 12345
total = 0

while a > 0:
    total += a % 10
    a //= 10


""" 
How it works: % 10 extracts the last digit, while // 10 removes the last digit. 
The process repeats until the number becomes 0.
Eg: 12345 → 5 → 4 → 3 → 2 → 1

Execution Flow: 

                a = 12345
                ↓
                12345 % 10 → 5
                12345 // 10 → 1234

                1234 % 10 → 4
                1234 // 10 → 123

                123 % 10 → 3
                123 // 10 → 12

                12 % 10 → 2
                12 // 10 → 1

                1 % 10 → 1
                1 // 10 → 0
                ↓
                5 + 4 + 3 + 2 + 1
                ↓
                15

"""