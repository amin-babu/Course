import json

def book_save(book_list):
  with open('book-file.json', 'w') as fp:
    json.dump(book_list, fp, indent=4)