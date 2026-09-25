# 1. check Palindrome using Slicing method

text = input("Enter a word: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


""" 
Execution flow:
                text = "madam"
                    ↓
                text[::-1]
                    ↓
                "madam"
                    ↓
                "madam" == "madam"
                    ↓
                True
                    ↓
                Palindrome
"""