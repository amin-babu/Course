def book_save(books):
  with open('books.csv', 'w') as file:
    for book in books:
      line = f"{book['title']}, {book['author']}, {book['isbn']}, {book['year']}, {book['price']}, {book['quantity']}\n"
      file.write(line)