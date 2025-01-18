import math
# 1. Baisc Calculator
#--------------------

#area of a circle
def AreaOfCircle(r):
  A = math.pi * (r ** 2)
  print(f"area of circle is {A:.2f}")
AreaOfCircle(5)

#area of rectangle
def areaOfrectangle(x,y):
  A = x * y
  print(f"area of rectangle is {A}")
areaOfrectangle(5, 6)

#area of Triangle
def areaOfTriangle(b, h):
  a = (b * h) / 2
  print(f"area of Triangle is {a}")
areaOfTriangle(7, 13)


# 2. Math Methods
#----------------

num = 17
newNum = math.sqrt(num)
print(newNum) #Squre Root
print(math.ceil(newNum))
print(math.pow(newNum, 2))