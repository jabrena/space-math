#
# https://projecteuler.net/problem=9
#
# Special Pythagorean triplet
# Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
#
# For example,
#
# 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Solution

def problem(limit):

    for a in range(1, limit):
        for b in range(1, limit):
            for c in range(1, limit):
                if (a + b + c == limit) and (a ** 2 + b ** 2 == c ** 2):
                    print("a: {} b: {} c: {}" . format(a, b, c))
                    return a * b * c

# Asserts
# print(problem(1000) == 31875000) #Computational issues for TI-84
