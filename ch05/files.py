#import os

file = open ("initialFile.txt", "w")
file.write("First Line \n")
file.write("Second Line")
file.close()
 

#os.listdir()

file = open("initialFile.txt", "r")
print(file.readline())
print(file.readline())
file.close() 