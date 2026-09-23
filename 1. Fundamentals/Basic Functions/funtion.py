def is_palindrome(text):
    # Reverse the string and compare with the original
    return text == text[::-1]


# Test cases
word = "madam"

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")