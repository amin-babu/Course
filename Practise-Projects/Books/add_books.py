import save_book
import isbn

def include_books(book_list):

  try:
    title = input('Enter Book Name : ')
    author = input('Enter Author Name : ')
    #book_isbn = isbn.isbn_check(book_list)
    year = int(input('Enter publishing year : '))
    price = int(input('Enter price : '))
    quantity = int(input('Enter quantity : '))
  except Exception as file:
    price

  book = {
    'title' : title,
    'author' : author,
    #'isbn' : book_isbn,
    'year' : year,
    'price' : price,
    'quantity' : quantity
  }

  book_list.append(book)
  save_book.book_save(book_list)
  print('Book Added Successfully')
  return book_list