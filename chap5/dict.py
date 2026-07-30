#Creating a Dictionary
d = {}
me = {
    'name':"Srushti",
    'age':20,
    'branch':'CSE',
    'CGPA':'9',
    'Clg':"DSATM",
    'girl':True,
    'skills':["HTML","CSS","Python","github"],
    'address': {'country': 'india', "city":" bnglr", "pincode":560021}
}
print(me)

#Dictionary Length: It checks the number of 'key: value' pairs in the dictionary.
print(len(me))

#We can access Dictionary items by referring to its key name.
print(me['name'])
print(me['CGPA'])
print(me.get('Clg'))
print(me.get('city'))   #instead of Error get-->None

#We can add new key and value pairs to a dictionary
me['job'] = "Student"
me['skills'].append('leetcode')
print(me)

#We can modify items in a dictionary
me['name'] = "Srushti Naik"
print(me)

#We use the in operator to check if a key exist in a dictionary
print('name' in me)
print('city' in me)


me.pop('girl')    #pop(key): removes the item with the specified key name
me.popitem()      #popitem(): removes the last item
del me['CGPA']    #del: removes an item with specified key name
print(me)

#Changing Dictionary to a List of Items:  The items() method changes dictionary to a list of tuples.
print(me.items())

#Clearing a Dictionary:  If we don't want the items in a dictionary we can clear them using clear() method
print(me.clear())

#Deleting a Dictionary: If we do not use the dictionary we can delete it completely
del me

#We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() 
print(dct_copy)

#Getting Dictionary Keys as a List:  The keys() method gives us all the keys of a a dictionary as a list.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)

#Getting Dictionary Values as a List: The values() method gives us all the values of a a dictionary as a list.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
value = dct.values()
print(value)