# Example to show how to define functions

def isOdd(x):
    if x % 2 == 0:
        return True
    return False


for x in range(10):
    print(x)
    print(isOdd(x))
