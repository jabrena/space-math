#
# https://projecteuler.net/problem=7
#
# 10001st prime
# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

# Solution

from sys import *


def getPrimeList(limit):

    primeList = []
    for num in range(2, maxsize):

        if (len(primeList) == limit):
            break

        for i in range(2, num):
            if (num % i == 0):
                break
        else:
            primeList.append(num)

    return primeList


def problem(limit):

    primerList = getPrimeList(limit)

    return max(primerList)


# Asserts
print(problem(6) == max((2, 3, 5, 7, 11, 13)))
# print(problem(10001) == 104743) #Computational issues for TI-84
