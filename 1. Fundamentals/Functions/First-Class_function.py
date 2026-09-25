def greet(name):
    return f"Hello, {name}"


# 1. Assign a function to a variable
say_hello = greet

print(say_hello("Arun"))
# Hello, Arun


# 2. Pass a function as an argument
def execute(func, name):
    return func(name)

print(execute(greet, "Priya"))
# Hello, Priya


# 3. Store a function in a list
functions = [greet]

print(functions[0]("Rahul"))
# Hello, Rahul


"""
Note:
        greet      # function object/reference
        greet()    # calls/executes the function

"""