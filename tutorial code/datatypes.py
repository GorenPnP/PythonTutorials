# there are a view basic datatypes in python

# int, str(string), float

# i will print it so you can see the result
f = 1.0003
print(f)
i = 1
print(i)
string = "This is a string"
print(string)

# we can cast between primitive Datatypes
integer = int(1.567)
print(integer)
# see? we made an integer from the float
string = "12345"
# we can cast a string to an int or integer
# we don´t need an extra variable ou can cast inside a function call
print(int(string))

# you can ask for the type of an variable with the type() call
print(type(f))
if type(f) == float:
    print("Its a float")

# when we cast a float to an integer, every number after the comma gets cut
print(int(f))
