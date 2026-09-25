# Reverse a String

text = input("Enter a string: ")

# 3. For loop method
reverse_3 = ""

for char in text:
    reverse_3 = char + reverse_3

print(reverse_3)

""" 
3. `for` Loop Method

The `for` loop goes through each character in the original string. 
Each character is added before the characters already stored, so the string gradually builds in reverse order. 
This method is useful in interviews because it demonstrates your understanding of loops and string manipulation.

"""

""" 
Execution Flow:
                text = "python"
                reverse_3 = ""
                        ↓
                char = "p"
                reverse_3 = "p" + "" → "p"
                        ↓
                char = "y"
                reverse_3 = "y" + "p" → "yp"
                        ↓
                char = "t"
                reverse_3 = "t" + "yp" → "typ"
                        ↓
                char = "h"
                reverse_3 = "h" + "typ" → "htyp"
                        ↓
                char = "o"
                reverse_3 = "o" + "htyp" → "ohtyp"
                        ↓
                char = "n"
                reverse_3 = "n" + "ohtyp" → "nohtyp"
                        ↓
                print(reverse_3)
                        ↓
                "nohtyp"
"""

