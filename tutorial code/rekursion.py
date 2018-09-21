"""
Recursion: minifying a problem bya self-calling function.
    (The calling Function waits for the called to come back)

example of a recursion of factorial, f for short:

function call      returns
f(4)            -> f(3) * 4
f(3)            -> f(2) * 3
f(2)            -> f(1) * 2
f(1)            -> f(0) * 1
f(0)            -> 1

so f(0) is done, we know that f(0) is equal to 1:
in reversed order, rippling through all functoin calls:

call            returns
f(0)            -> 1
f(1)            -> f(0) * 1 = 1 * 1 = 1
f(2)            -> f(1) * 2 = 1 * 2 = 2
f(3)            -> f(2) * 3 = 2 * 3 = 6
f(4)            -> f(3) * 4 = 6 * 4 = 24

Attention! you need a reachable exit point (such as if not n: return 1)
that does not call the function again, otherwise these little functions won't terminate
"""
def factorial(n):
    """input: int >= 0, calculates n! recursively"""
    if not n:
        return 1
    return factorial(n-1) * n

def fibonacci(n):
    """input: int >= 0, calculates the n-th fibonacci-num (including 0) recursively"""
    if not n:
        return 1
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

"""
A pretty example of what recursions can be capable of:

towers of hanoi:
      |               |               |
     x|x              |               |
    xx|xx             |               |
   xxx|xxx            |               |
  xxxx|xxxx           |               |
-------------   -------------   -------------
  Start (A)      Zwischen (B)      Ziel (C)

goal: move all disks one by one from Start to Ziel and use Zwischen as intermediate. A larger disk must never be on top of a smaller one.
"""
def hanoi(n, start, zwischen, ziel):
    if n:
        hanoi(n-1, start, ziel, zwischen)
        print("Zug: Scheibe von {} nach {}".format(start, ziel))
        hanoi(n-1, zwischen, start, ziel)


# this is the man part of the program. Time to play around ;)
print("factorial: (should be 6)", factorial(3))
print("fibonacci: (should be 8)", fibonacci(5))
hanoi(n=4, start="A", zwischen="B", ziel="C")

