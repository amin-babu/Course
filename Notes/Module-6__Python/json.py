import json

# object to json
#---------------

"""
personObj = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "hasChildren": False,
  "titles": ["engineer", "programmer"]
}

personJSON = json.dumps(personObj)


print(personJSON)
"""











# json to object
#---------------

"""
personJSON = '{"name": "John", "age": 30, "city": "New York", "hasChildren": false, "titles": ["engineer", "programmer"]}'

personOBJ = json.loads(personJSON)

print(type(personJSON))
print(type(personOBJ))
"""








# object to json write in file
#-----------------------------

personObj = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "hasChildren": False,
  "titles": ["engineer", "programmer"]
}

with open('person.json', 'w') as file:
  json.dump(personObj, file, indent=4)










# json to object read from file
#------------------------------

"""
with open('person.json', 'r') as file:
  personOBJ = json.load(file)
  personJSON = json.dumps(personOBJ, indent=4)
  print(personJSON)
"""