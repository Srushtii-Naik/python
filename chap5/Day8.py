#Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name':'Tommy',
    'color': 'brown',
    'breed': 'Golden Retriever',
    'legs' : 4,
    'age' : 5
}
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Srushti',
    'last_name' : 'Naik',
    'gender':"Female",
    "age":20,
    "skills":["HTML","CSS","Python","github"],
    "address":{"country":"india","city":"banglore"}
}

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

#Modify the skills values by adding one or two skills
student['skills'].append("leetcode")
print(student)

#Get the dictionary keys as a list
print(student.keys())

#Get the dictionary values as a list
print(student.values())

#Change the dictionary to a list of tuples using items() method
dict = student.items()
print(dict)
print(type(dict))

#Delete one of the items in the dictionary
student.pop('address')
print(student)

#Delete one of the dictionaries
del dog
print(dog)