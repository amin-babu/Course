import json
import os

def see_books():
  if not os.path.exists('book-file.json'):
      print("File is not Exist")
      return

  with open('book-file.json', 'r') as fp:
    try:
        book_list = json.load(fp)
    except Exception as e:  # Handles cases where the file exists but is empty or contains invalid JSON
        print("Empty")
        return

    if book_list:  # Checks if the list is not empty
        for book in book_list:
            print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added: {book['bookAdded_at']}")
