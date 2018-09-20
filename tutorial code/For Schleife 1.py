import time as t
# i is our counter variable
# the range() function generates a list from the input parameters from the start to one below the defined end
# example: range(2,10) would generate the following list 2,3,4,5,6,7,8,9
for i in range(1, 10):
    print(i)


mason = False
# You can use range to iterate over Lists with known size
if mason:
    g = ["Mason", "ist", "ein", "Spasst", "und", "er", "ist", "Dumm", "und", "Scheiße"]
    # the range function can be used with only one Parameter his defines the end point, range starts automatic with start = 0
    for i in range(10):
        print(g[i])
    # this suspends exection for 3 seconds
    t.sleep(3)
    # and with the help of len() over Lists with unknown size
    for i in range(len(g)):
        print(g[i])

string_mason = False
if string_mason:
    # now we iterate over Strings
    # this is just an example String
    string = "Hallo was geht"
    for i in string:
        print(i)
    # the same with the len() function
    for i in range(len(string)):
        print(string[i])

cast_mason = False

if cast_mason:
    # now we cast each number to an int
    # int() takes one parameter a string or a float or so
    o = "125423"
    for i in o:
        j = int(i)
        print(j)

    # we can add the Number after casting
    ir = 0
    for i in o:
        ir = ir + int(i)


# now you make your own function, it takes every character from a string and calaculates the cross sum
# i will give you a string prebuild
pre_build = "9435824323432"
# you are free to use any methods andd variables


