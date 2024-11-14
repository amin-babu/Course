# Task 2: String Manipulation


#String Slicing
country = 'bangladesh'
print(country[:3])  #Print first three characters
print(country[-3:]) #Print last three characters
print(country[::-1]) #Print the string in reverse order.

#String Methods
text = 'this is a uppercase'
print(text.upper()) #Convert it to uppercase
text = 'THIS IS A LOWERCASE'
print(text.lower()) #Convert it to lowercase

#Replace a letter in the string
name = 'Hablo'
print(name.replace('o', 'a'))
print(name.find('b')) #Find position of a specific character

#Palindrome Check
def is_palindrome(word):
  country = word
  palindrom = country[::-1]
  if country == palindrom:
    print(f"{country} is a palindrom word")
  else:
    print(f"{country} is not a palindrom word")

is_palindrome('babu')