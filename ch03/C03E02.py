# This example show how use different data types

from time import sleep

# Definition
dataType1 = str("Hello World")
dataType2 = "Hello World"
dataType3 = int(20)
dataType4 = 20
dataType5 = float(20.5)
dataType6 = 20.5
dataType7 = list(("apple", "banana", "cherry"))
dataType8 = ("apple", "banana", "cherry")
dataType9 = range(6)
dataType10 = set(("apple", "banana", "cherry", "banana"))
dataType11 = bool("true")
dataType12 = True

dataTypes = (dataType1, dataType2, dataType3, dataType4, dataType5, dataType6,
             dataType7, dataType8, dataType9, dataType10, dataType11, dataType12)

# Iteration
for i in dataTypes:
    print(type(i))
    print(i)
    sleep(1)
