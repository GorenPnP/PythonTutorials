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

# now thats all i actually know about the python formatting, may updating it in future
