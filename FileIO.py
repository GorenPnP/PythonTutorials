import os

# check if the file File.txt exists
if os.path.exists("File.txt"):
    # r+ is the mode we open it in READ mode but CAN write to it, if the file not exist it will not created
    f = open("File.txt", "r+")
else:
    # w opens the file , create it if it not exist, and trash the file if it´s exist
    f = open("File.txt", "w")

# create a list that gets written to the file
# \n is an extra character marks the beginning of a newline
arr = ["Hallo\n", "Was\n", "Geht\n"]
# this method takes a list as a parameter
f.writelines(arr)

# you can iterate over nearly EVERYTHING in python
# now we read from that file the lines back
for i in f:
    print(i)

# We create an empty list to write the content of the file
array = []
# we iterate over the file and add it line by line to the list "array"
for i in f:
    array += i

