# This example show how to use the bifurcation

var1 = 5

#Block if
if var1 >= 5 :
    print("Passed")

#Block if else
if var1 % 2 == 0 :
    print("Even")
else :
    print("Odd")

#Block if elif else
if var1 == 0 :
    print("Disaster")
elif var1 >= 5 :
    print("Passed")
else :
    print("Unknown state")