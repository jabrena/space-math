#
# https://projecteuler.net/problem=4
#
# Largest palindrome product
# Problem 4
# 
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digits numers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Solution

def reverse(a_string):
    new_string = ''
    index = len(a_string)
    while index:
        index -= 1                    # index = index - 1
        new_string += a_string[index] # new_string = new_string + character
    return new_string

def isPalindrome(value):
    s = str(value)
    #return s == s[::-1] #It is not valid in Micro Python
    return s == reverse(s)

def problem(limit) :

    maxPalindrome = 0
    for x in range(limit) :
        for y in range(limit) :
            value = x * y
            if isPalindrome(value) :
                if (value > maxPalindrome) :
                    #print(value)
                    maxPalindrome = value

    return maxPalindrome

# Asserts
print(reverse("demo") == "omed")
print(isPalindrome(9008) == False)
print(isPalindrome(9009) == True)
print(problem(100) == 9009)
#print(problem(1000) == 906609) #Computational issues for TI-84