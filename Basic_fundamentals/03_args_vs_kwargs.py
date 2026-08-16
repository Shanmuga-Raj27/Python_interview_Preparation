

def func(a, *args, **kwargs):
    print("positional:", a)
    print("extra positional:", args)        # tuple
    print("keyword:", kwargs)               # dict

func(1, 2, 3, 4, name="Alice", age=30)



"""
What are *args and **kwargs in Python?

Answer:

*args allows a function to accept a variable number of positional arguments and stores them as a tuple.
**kwargs allows a function to accept a variable number of keyword arguments and stores them as a dictionary.
They are useful when a function needs to accept flexible or unknown numbers of arguments.

"""