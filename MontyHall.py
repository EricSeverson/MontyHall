"""
This Program will simulate the Monty Hall problem
over a large iteration to test its validity.
"""

from random import randint

iterations = int(input("Please Enter the Number of Iterations you would like to use: "))
# doors[0] holds goats, doors[1] holds car
doors = [[0, 0], 0]
num1correct = 0
num2correct = 0

for x in range(iterations):
    doors[0][0] = randint(1, 3)
    doors[0][1] = randint(1, 3)
        
    while doors[0][0] == doors[0][1]:
        doors[0][1] = randint(1, 3)

    doors[1] = 6 - (doors[0][0] + doors[0][1])
    choice1 = randint(1, 3)
    opened = doors[0][randint(0, 1)]
    while opened == choice1:
        opened = doors[0][randint(0, 1)]

    choice2 = 6 - (opened + choice1)
    if choice1 == doors[1]:
        num1correct += 1
    elif choice2 == doors[1]:
        num2correct += 1

print("Without switching: %", num1correct/iterations * 100, " Correct")
print("With switching: %", num2correct/iterations * 100, " Correct")
