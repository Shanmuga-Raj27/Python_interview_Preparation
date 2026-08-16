x = [1, 2, 3]  # Creates a new list object
y = [1, 2, 3]  # Creates another separate list object

z = x           # z does NOT create a new list, z points to the same object as x #


print(x is y)      # False → x and y are different objects, Even though their values are the same
print(x == y)      # True → the values inside x and y are the same


print(z is x)     # True → z and x point to the SAME object
print(z == x)      # True → obviously, they have the same values


print(id(x))
print(id(y))       # Different ID → different object

print(id(z))      # Same ID as x → same object

""" 
Interview Question: What is the difference between `is` and `==` in Python?

Answer:
`==`  - compares whether two objects have the same value.
`is`  - checks whether two variables refer to the same object in memory.
`id()` -  can be used to check an object's unique identity.

"""