#
# https://projecteuler.net/problem=3
#
# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# Solution

# Inspiration from: https://stackoverflow.com/questions/15347174/python-finding-prime-factors
def problem(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


# Asserts
print(problem(13195) == 29)
print(problem(600851475143) == 6857)
