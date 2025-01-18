#Task 4: Control Flow (If-Else, Logical Operators)

print('Click 1 to check num, Click 2 for loan')
choose = int(input('Choose a option : '))

if choose == 1:
  num = int(input('Enter a Number : '))

  if num > 0:
    if num % 2 == 0:
      print(f"{num} is even and positive number")
    else:
      print(f"{num} is odd and positive number")
  elif num < 0:
    if num % 2 == 0:
      print(f"{num} is even and negative number")
    else:
      print(f"{num} is odd and negative number")
  else:
    print(f"{num} is Zero")

elif choose == 2:

  age = int(input('Enter your age : '))
  credit_score = int(input('Enter your credit score : '))
  annual_income = int(input('Enter your annual income : '))

  if (age > 18) and (credit_score > 600) and (annual_income > 30000):
    print('You are Eligible for loan')
  else:
    print('You are not Eligible for loan')

else:
  print('Invalid Choise')