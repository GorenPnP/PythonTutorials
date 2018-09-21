import math

# short program discription and input requirements
print("Dieses Programm liest eine ganze Zahl n > 0 ein und ermittelt ob es",      "sich bei dieser um eine Primzahl handelt oder nicht.",
      "\nBitte eine nat. Zahl eingeben:")


# valriable declarations:
#   validInput: make sure to exit the following while-loop only if input was valid and stored in num as int
#   num: contains the read input value (initialized with -1 for no reason, could be any int really)
validInput = False
num = -1

while not validInput:

    # think positive
    validInput = True

    # gets input from user and stores resulting string in inStr
    inStr = input(">> ")

    # try to cast str to an int
    try:
        # if that did not work it was not valid and a ValueError occurs from 'int(inStr)'. Jumps right ..
        num = int(inStr)
    except ValueError as e:
        # .. here.
        print("Das war keine ganze Zahl. Penner")
        # start from head of while-loop again
        validInput = False
        continue
    
    # num is now an int and should be >= 0
    if num < 0:
        print("Die Zahl ist negativ. Eine Zahl >= 0 wäre schon noice.")
        validInput = False


prime = True

# valid input since here. Calculation incoming

# ideas for improvement:
#   check if two, else if num is even it is not prime
#   check only odd numbers to be a factor for num
#   check until sqrt(num), because for max(x, y) for x*y=num is maximal
#       for all x, y
if num % 2 == 0 and num > 2:
    prime = False

middle = math.ceil(math.sqrt(num))
# if min > max in range function for is never executed (as in 3 > 2)
# 3rd argument is the step width, remember: odd numbers are sufficent here
for i in range(3, middle, 2):
    if not prime or num % i == 0:
        prime = False
        break

print(prime)
