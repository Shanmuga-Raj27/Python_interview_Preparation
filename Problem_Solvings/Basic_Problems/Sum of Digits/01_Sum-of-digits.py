# Sum of Digits

a = 12345

# 1. Pythonic approach — sum() + map()
print(sum(map(int,str(a))))


"""
How it works: str(a) converts the number into a string, map(int, ...) converts each digit back to an integer, 
and sum() adds all the digits. This is the shortest and most Pythonic solution.

Execution Flow:
                  a = 12345
                     ↓
                  str(a)
                     ↓
                  "12345"
                     ↓
                  map(int, ...)
                     ↓
                  1 → 2 → 3 → 4 → 5
                     ↓
                  sum(...)
                     ↓
                  1 + 2 + 3 + 4 + 5
                     ↓
                  15

"""