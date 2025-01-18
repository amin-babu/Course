import save_book
import datetime
import os
import json

def change_book():
  if not os.path.exists('book-file.json'):
    print("File is not Exist")
    return
  
  with open('book-file.json', 'r') as fp:
    try:
        book_list = json.load(fp)
    except Exception as e:  # Handles cases where the file exists but is empty or contains invalid JSON
        print("Empty")
        return

  
  while True:
    try:
      isbn = int(input('Enter ISBN to update: '))
      break
    except ValueError:
      print('Please enter valid integer')
  found = False

  for book in book_list:
    if isbn == book['isbn']:
      found = True
      book['title'] = input('Enter title: ') or book['title']
      book['author'] = input('Enter author name: ') or book['author']

      while True:
        try:
          book['year'] = int(input('Enter year: '))
          break
        except ValueError:
          print('Enter valid Integer')

      while True:
        try:
          book['price'] = int(input('Enter price: '))
          break
        except ValueError:
          print('Enter valid Integer')

      while True:
        try:
          book['quantity'] = int(input('Enter quantity: '))
          break
        except ValueError:
          print('Enter valid Integer')
      
      book['bookUpdated_at'] = datetime.datetime.now().strftime('%d-%h-%Y')

      save_book.book_save(book_list)
      print('Book Updated')
      return
    
  if not found:
    print('Book Not Found')
    return

