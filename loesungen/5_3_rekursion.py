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
def ackermann(n, m):
    if not n:
        return m + 1
    if not m:
        return ackermann(n-1, 1)
    return ackermann(n-1, ackermann(n, m-1))

def isPalindrome(word):
    # either the length of word is 1 or 0, so it is a palindrome by definition
    if len(word) < 2:
        return True
    lastCharAt = len(word) -1
    # word[0] is the first character, word[lastCharAt] is the last one
    if word[0] == word[lastCharAt]:
        # smaller word, without the first and the last character
        return palindrom(word[1:-1])
    return False

def potenz(base, exponent):
    # equivalent to: if exponent is None or exponent == 0
    if not exponent:
        return 1
    return potenz(base, exponent - 1) * base

def factorial(n):
    if not n:
        return 1
    return factorial(n-1) * n

def fibonacci(n):
    if not n:
        return 1
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print("isPalindrome lagerregal: (should be True)", isPalindrome("lagerregal"))
print("ackermann: (should be 4)", ackermann(1, 2))
print("potenz: (should be 8)", potenz(2, 3))
print("factorial: (should be 6)", factorial(3))
print("fibonacci: (should be 8)", fibonacci(5))
