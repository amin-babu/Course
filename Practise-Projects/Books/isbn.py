def isbn_check(content):
  
  if content == []:
    isbn = int(input('Enter ISBN : '))
    return isbn
  
  else:
    while True:
      isbn = int(input('Enter ISBN2 : '))
      for book in content:
        if book['isbn'] == isbn:
          print('ISBN already taken')
        else:
          return isbn
