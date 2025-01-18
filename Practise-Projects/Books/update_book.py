import save_book

def change_book(book_list):
  isbn = int(input('Enter ISBN : '))

  for book in book_list:
    if book['isbn'] == isbn:
      print(f"Current Book is {book}")
      book['title'] = input('Enter new title name : ') or book['title']
      book['author'] = input('Enter new author name : ') or book['author']
      # book['isbn'] = input('Enter new isbn : ') or book['isbn']
      print('ISBN number cannot be changed')
      book['year'] = input('Enter new publishing year : ') or book['year']
      book['price'] = input('Enter new price : ') or book['price']
      book['quantity'] = input('Enter new quantity : ') or book['quantity']
  
      print('Book updated successfully')
      save_book.book_save(book_list)
      return book_list
  
  print('No Book Found')
  return book_list