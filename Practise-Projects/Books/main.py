from add_books import include_books
import update_book

all_books = []

while True:
  print('Welcome to Library Management System')
  print('0. Exit')
  print('1. Add Books')
  print('2. Update Book')
  print('3. Remove Book')
  print('4. View All Books')

  select = int(input('Select an option : '))

  if select == 0:
    print('Thanks for using Library Management System')
    break

  elif select == 1:
    all_books = include_books(all_books)
  
  elif select == 2:
    all_books = update_book.change_book(all_books)