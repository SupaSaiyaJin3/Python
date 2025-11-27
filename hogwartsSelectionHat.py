#Point count
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

#Intro 
print('=================')
print('The Sorting Hat')
print('=================\n')

# Question 1
print("\nAnswer with 1 or 2.\n")
question1 = int(input('Q1) Do you like Dawn or Dusk? \n\n1) Dawn \n2) Dusk \n\n'))

if question1 == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif question1 == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
else:
  print('\nWrong input.')

#Question 2
print("\nAnswer with 1, 2, 3 or 4.")
question2 = int(input("\nQ2) When I'm dead, I want people to remember me as: \n 1) The Good \n 2) The Great \n 3) The Wise \n 4) The Bold \n\n"))

if question2 == 1:
  hufflepuff = hufflepuff + 2
elif question2 == 2:
  slytherin = slytherin + 2
elif question2 == 3:
  ravenclaw = ravenclaw + 2
elif question2 == 4:
  gryffindor = gryffindor + 2
else:
  print("\nWrong input.")

#Question 3
print("\nAnswer with 1, 2, 3 or 4.")
question3 = int(input("\nQ3) Which kind of instrument most pleases your ear? \n 1) The violin \n 2) The trumpet \n 3) The piano \n 4) The drum \n\n")) 

if question3 == 1:
  slytherin = slytherin + 4
elif question3 == 2:
  hufflepuff = hufflepuff + 4
elif question3 == 3:
  ravenclaw = ravenclaw + 4
elif question3 == 4:
  gryffindor = gryffindor + 4
else:
  print("\nWrong input.")

#Results
print("\nThe final results are...\n")
print("Slytherin = \n", slytherin)
print("Hufflepuff = \n", hufflepuff)
print("Ravenclaw = \n", ravenclaw)
print("Gryffindor = \n", gryffindor)

#Bonus Part
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print('\n🦁 Gryffindor!\n')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('\n🦅 Ravenclaw!\n')
elif hufflepuff >= slytherin:
  print('\n🦡 Hufflepuff!\n')
else:
  print('\n🐍 Slytherin!\n')