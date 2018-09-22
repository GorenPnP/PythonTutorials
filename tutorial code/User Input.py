# now we will talking about user input and interaction

# we will start with the input function

print("Start give a Number:")
# we start by get the input from the user
input_result = input()
# and print it
print("Your Number was: ", input_result)
# we can even make a prompt so we dont need to print before asking the user for input
input_result = input("Provide something other: ")
print("You provided:", input_result)


valid = True
# loop until the user gives a sequenz of numbers
while valid:
    try:
        # we ask the user for input
        casted_input = int(input("please provide something: "))
        valid = False
    except ValueError:
        # if the user not gave us an int
        print("Not an int")
# we check if we have an int
if type(casted_input) == int:
    print("Perfect you gave me an int")
else:
# and will be surprised if its not the case
    print("How the fuck did you done this?")

