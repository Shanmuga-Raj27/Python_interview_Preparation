
# check Anagram using sorted() method. 
a = "listen"
b = "silent"

if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")



""" 
Anagram: 

    Two strings are anagrams if they contain the same characters with the same frequency, but in a different order.
"""
""" 
How it works: 
                a = "listen"                  b = "silent"
                    ↓                                ↓
                    sorted()                       sorted()
                    ↓                                ↓
                ['e','i','l','n','s','t']     ['e','i','l','n','s','t']
                                            ↓
                                        Compare
                                            ↓
                                        Equal
                                            ↓
                                        Anagram

Note: sorted() arranges the characters in the same order. If both sorted lists are equal, 
the original strings contain the same characters with the same frequencies.
"""