#
# https://projecteuler.net/problem=6
#
# Sum square difference
# Problem 6
#
# The sum of the squares of the first ten natural numbers is:
#
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is:
#
# (1 + 2 + ... + 10) ^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
#
# 3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Solution

def squareSum(limit):

    listSquared = []
    for x in range(1, limit + 1):
        listSquared.append(x ** 2)

    return sum(listSquared)


def sumSquare(limit):

    listSquared = []
    for x in range(1, limit + 1):
        listSquared.append(x)

    return sum(listSquared) ** 2


def problem(limit):

    return sumSquare(limit) - squareSum(limit)


# Asserts
print(squareSum(10) == 385)
print(sumSquare(10) == 3025)
print(problem(100) == 25164150)
