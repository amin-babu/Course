favourite_food = []

while True:
  print('Welcome to Favourite Food Manager')
  print('1. Exit')
  print('2. Add Food')
  print('3. Remove Food')
  print('4. View All Food')

  option = int(input('Select an option : '))

  if option == 1:
    print("Thanks for using Favourite Food Manager App")
    break

  elif option == 2:
    add_food = input('Enter favourite food name : ')
    favourite_food.append(add_food)
    print(f"{add_food} is added")

  elif option == 3:
    try:
      remove_food = input('Enter which you want to remove : ')
      favourite_food.remove(remove_food)
      print(f"{remove_food} is removed")
    except Exception as e:
      print(e)

  elif option == 4:
    if favourite_food != []:
      for num, f_name in enumerate(favourite_food, start=1):
        print(f"{num}. {f_name}")
    else:
      print(f"Food List is empty")
  
  else:
    print(f"Select a valid Option")
