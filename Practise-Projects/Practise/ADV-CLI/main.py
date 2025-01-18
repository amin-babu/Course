import add_book
import view_book
import update_book

book_list = []

while True:
  print('Welcome to ADV-CLI')
  print('0. Exit')
  print('1. Add Books')
  print('2. View All Books')
  print('3. Books Update')
  print('4. Book Remove/Delete')
  print('5. Lend a Book')
  print('6. Return a Book')

  menu = input('Select an option: ')

  if menu == '0':
    print('Thanks for using ADV-CLI')
    break

  elif menu == '1':
    book_list = add_book.include_book(book_list)

  elif menu == '2':
    view_book.see_books()
  
  elif menu == '3':
    update_book.change_book()