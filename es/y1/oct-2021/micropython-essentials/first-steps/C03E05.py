# This example show how to use the iteration

from time import sleep

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

sleep(1)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

sleep(1)

for x in range(5):
    print(x)

sleep(1)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

sleep(1)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

sleep(1)

count = 0
while count < 5:
    print(count)
    count += 1

sleep(1)

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
