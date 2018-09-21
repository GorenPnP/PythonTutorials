# there are a few control structures
# control structures are if, for, while, try

# if is the simplest:
x = True
# we test if x is true
if x:
    print("x is true")

# we test if x is not False
if x is not False:
    print("x is true")

x = False
# we test if x is true, which should not be the case
if x:
    print("x is true")

# we test if x is not True and because x is false this must be true
if x is not True:
    print("X is false")

tmp = 0

# a while loop does something until the predifened condition returns false

while tmp < 100:
    print(tmp)
    tmp = tmp + 1

# you can create an endless loop by writing while True: your code...
# some Integrated development enviremonts will give you an error if you have no break standment

tmp = 0
while True:
    tmp = tmp + 1
    if tmp == 100:
        break

# some ides are so smart they detect if a condition can be reached, and if not gives you errors, (Thanks Eclipse)

# for loops:
# a for loop is used to iterate over nearly everything in python: strings, lists, sets, files. etc
for i in ["Hello", "World,", " how", " are", "you"]:
    print(i)

# easy or?
