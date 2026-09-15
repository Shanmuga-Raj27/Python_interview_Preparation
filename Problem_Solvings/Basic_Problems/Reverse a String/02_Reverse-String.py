# Reverse a String

text = input("Enter a string: ")

# Reversed function method
reverse_2 = "".join(reversed(text))
print(reverse_2)

""" 
2. `reversed()` Function Method

The `reversed()` function reads the string characters from last to first and returns them as a reverse iterator. 
The `join()` method then combines those characters into a single string. 
This method is also simple and commonly accepted in interviews.

"""

""" 
Execution Flow: 

                text = "python"
                        ↓
                reversed(text)
                        ↓
                "n" → "o" → "h" → "t" → "y" → "p"
                        ↓
                "".join(...)          # join() combines characters
                        ↓
                "nohtyp"
                        ↓
                print(reverse_2)
                        ↓
                nohtyp
"""