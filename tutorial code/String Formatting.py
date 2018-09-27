# we create a string with two {}, this is a formatting equivalent to C's %s,%i etc...
string = "{} are cool"

# we format it, that means we replace {} with "You"
string = string.format("You")
# and print it
print(string)

# you can format it inline so you can save a little bit of lines and keep readability
string = "{} are cool because {}".format("You", "you are learning python")
print(string)

# it can be done with an unlimited amount of arguments
string = "{} {} {} {} {} {} {} {} {} {} {} {} {} {}".format("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "You understand?")
print(string)

# you can change the indexes with numbers, if you are writing it like this: {1} {2} {0} you need to write .format("cool?", "Are", "you")
string = "{1} {0} {2}".format("are", "You", "cool")
print(string)

# you can give your {} placeholder names and can address them directly
string = "{one} {two}".format(one="Hello", two="World")
print(string)

string = "{third} {first} {second}".format(first="is", third="This", second="nice")
print(string)

# you can add whitspaces if the string is under 10 characters long, you can use len() to get the string lenght
string = "{:10} See?".format("Hello")
print(string)


# a little bit of object orientated programming
class Foo(object):
    def __format__(self, format):
        if (format == "python_is_awesome"):
            return "Python is really nice"
        return 'HAL 9000'


string = "{:python_is_awesome}".format(Foo())


# now thats all i actually know about the python formatting, may updating it in future
