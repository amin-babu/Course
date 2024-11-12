print("Welcome to calculator project")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input('Select an operation to calculate basic operation: '))

#Addition
if option == 1:
  n1 = int(input('Enter 1st number: '))
  n2 = int(input('Enter 2nd number: '))
  n3 = n1 + n2
  print("Addition is " + str(n3))

#Subtraction
elif option == 2:
  n1 = int(input('Enter 1st number: '))
  n2 = int(input('Enter 2nd number: '))
  n3 = n1 - n2
  print("Subtraction is " + str(n3))

#Multiplication
elif option == 3:
  n1 = int(input('Enter 1st number: '))
  n2 = int(input('Enter 2nd number: '))
  n3 = n1 * n2
  print ("Multiplication is " + str(n3))

#Division
elif option == 4:
  n1 = int(input('Enter 1st number: '))
  n2 = int(input('Enter 2nd number: '))
  n3 = n1 / n2
  print("Division is " + str(n3))

else:
  print('Invaild Input')