lengthA = int(input("What is the length of the A side? "))
lengthB = int(input("What is the length of the B side? "))
hypotenuse = int(input("What is the length of the hypotenuse? "))

c = (lengthA ** 2 + lengthB ** 2) ** 0.5

print('The answer is ' + str(c))