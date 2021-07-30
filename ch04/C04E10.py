#
# https://projecteuler.net/problem=10
#
# Summation of primes
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# Solution

from sys import *

def getPrimeList(limit) :

    primeList = []
    for num in range(2, limit) :
        for i in range(2, num) :
            if (num % i == 0) :
                break
        else:
            if (num > limit) :
                break
            print(num)
            primeList.append(num)

    print(primeList)
    return primeList


def problem(limit) :
    
    return sum(getPrimeList(limit))

# Asserts
print(getPrimeList(10) == list((2, 3, 5, 7)))
print(problem(10) == 17)
#print(problem(2000000) == 142913828922) #Computational issues for TI-84