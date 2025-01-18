import save_book
import random
import datetime

def include_book(the_books):
  title = input('Enter the title: ')
  author = input('Enter author name: ')
  isbn = random.randint(10000, 99999)

  while True:
    try:
      year = int(input('Enter year: '))
      break
    except ValueError:
      print('Please Enter valid integer')

  while True:
    try:
      price = int(input('Enter price: '))
      break
    except ValueError:
      print('Please Enter valid integer')

  while True:
    try:
      quantity = int(input('Enter quantity: '))
      break
    except ValueError:
      print('Please Enter valid integer')
  
  bookAdded_at = datetime.datetime.now().strftime('%d-%h-%Y')

  book = {
    'title': title,
    'author': author,
    'isbn': isbn,
    'year': year,
    'price': price,
    'quantity': quantity,
    'bookAdded_at': bookAdded_at,
    'bookUpdated_at': ''
  }

  the_books.append(book)
  save_book.book_save(the_books)
  print('Book Added Successfully!')
  return the_books