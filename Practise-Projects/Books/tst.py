title = input('Enter Book Title : ')
author = input('Enter Author Name : ')
try:
  isbn = int(input('Enter ISBN Number : '))
  year = int(input('Enter Publishing Year Number : '))
  price = int(input('Enter Book Price : '))
  quantity = int(input('Enter Quantity Number : '))
except ValueError:
  print('This input must be an interge')