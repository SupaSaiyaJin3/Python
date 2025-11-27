def get_item(option):
  if option == 1:
    return '🍔 Cheeseburger'
  elif option == 2:
    return '🍟 Fries'
  elif option == 3:
    return '🥤 Soda'
  elif option == 4:
    return '🍦 Ice Cream'
  elif option == 5:
    return '🍪 Cookie'
  else:
    return 'Sorry that item is not on the menu...'   

def welcome():
  return "Welcome to McDonalds, what can I get for you today? \n\nHere are our options: \n\n#1 Cheeseburger \n#2 Fries \n#3 Soda \n#4 Ice Cream \n#5 Cookie\n"


print(welcome())
option = int(input('What would you like to order? '))
print(get_item(option))