#Task 1: Variables, Data Types, and Conversions

numInt = 10
numFloat = 20.36
boolean = False
strings = 'Bangladesh'
fruitsList = ['mango', 'bananna', 'apple']

#Int to float by printing format
int_toFloat = float(numInt)
print("Float = {}, Type = {} ".format(int_toFloat, type(int_toFloat)))

#Float to Int
float_toInt = int(numFloat)
print("Int = {}, Type = {}".format(float_toInt, type(float_toInt)))

#Boolean to String
bln_toSTR = str(boolean)
print("String = {}, Type = {}".format(bln_toSTR, type(bln_toSTR)))

#String To List
str_toList = list(strings)
print("{} => Type {}".format(str_toList, type(str_toList)))

#list to tupels
list_toTupel = tuple(fruitsList)
print("{} => Type {}".format(list_toTupel, type(list_toTupel)))