# 1a) faculty with for-loop
def fak_for(n):
    if n < 0:
        return -1
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

# 1b) faculty with while-loop
def fak_while(n):
    if n < 0:
        return -1
    prod = 1
    while n:
        prod *= n
        n -= 1
    return prod

# 1c) faculty recursively
def fak_rek(n):
    if n < 0:
        return -1
    if n == 0:
        return 1
    return fak_rek(n-1) * n

# sum is esentially the same as faculty, only with + instead of * and another base case, 0 instead of 1.

# 2a) sum with for-loop
def sum_for(n):
    if n < 0:
        return -1
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

# 2b) sum with while-loop
def sum_while(n):
    if n < 0:
        return -1
    sum = 0
    while n:
        sum += n
        n -= 1
    return sum

# 2c) sum recursively
def sum_rek(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    return sum_rek(n-1) + n

# 3a) b to the power of e with for-loop
def power_for(b, e):
    if e < 0:
        return -1
    power = 1
    for i in range(e): # len( range(e) ) == len( range(1, e+1) )
        power *= b
    return power

# 3b) b to the power of e with while-loop
def power_while(b, e):
    if e < 0:
        return -1
    power = 1
    while e:
        power *= b
        e -= 1
    return power

# 3c) b to the power of e recursively
def power_rek(b, e):
    if e < 0:
        return -1
    if e == 0:
        return 1
    return power_rek(b, e-1) * b


# start of main program
if __name__ == "__main__":
    for i in range(-1, 5):
        print("fak_for({}) returns {}".format(i, fak_for(i)))
        print("fak_while({}) returns {}".format(i, fak_while(i)))
        print("fak_rek({}) returns {}\n".format(i, fak_rek(i)))

        print("sum_for({}) returns {}".format(i, sum_for(i)))
        print("sum_while({}) returns {}".format(i, sum_while(i)))
        print("sum_rek({}) returns {}\n".format(i, sum_rek(i)))

        print("power_for(2, {}) returns {}".format(i, power_for(2, i)))
        print("power_while(2, {}) returns {}".format(i, power_while(2, i)))
        print("power_rek(2, {}) returns {}".format(i, power_rek(2, i)))
        print("-------------------------------")


