# short program discription and input requirements
print("Dieses Programm liest eine ganze Zahl n > 0 ein und berechnet",
      "die Quersumme der Zahl. Bitte eine nat. Zahl eingeben:")


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


# valid input since here. Calculation incoming

sum = 0

# equivalent to: while (num is not None) and (num != 0)
while num:

    # add last digit of num to sum
    sum += num % 10

    # cut last digit off
    num //= 10

# print solution
print("Die Quersumme ist", sum)
