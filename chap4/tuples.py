# A tuple is an ordered, immutable (cannot be changed) collection.
#creating
points = (10,20)
colors = ("red","green","blue")

#Indexing
print(points[1])
print(colors[1])

#Slicing
print(colors[:2])
print(colors[-2:])

#tuples: Only two methods
nums = (10,56, 23, 10, 24,7 ,45)
print(nums.count(10))
print(nums.index(24))

#Packing and Unpacking (Interview Favorite)
me = ("Srushti",20,"CSE")
name, age, branch = me
print(name)
print(age)
print(branch)

#Can a Tuple contain Lists? Yes. (tuples!=change but lists=change)
t = ([1,2],[3,4])
t[0].append(3)
print(t)
t[1].pop()
print(t)



#Interview Questions
'''
Tuple: Immutable, 
uses (), 
fewer methods, 
faster, 
used for fixed data.'''

'''
When should you use a Tuple instead of a List?
Use a tuple when the data should not change
eg coordinates, RGB colors, dates 
bcz it prevents accidental modification
'''

# ___________________________________________________________________________________________________________________________________________________________________________________


#Empty tuple: Creating an empty tuple
t = ()
t = tuple()

#Tuple with initial values
fruits = ('banana', 'orange', 'mango', 'lemon')

#We use the len() method to get the length of a tuple.
print(len(fruits))

#Positive Indexing Similar to the list data type we use positive or negative indexing to access tuple items.
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[0])
print(fruits[3])

#Negative indexing Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last and the negative of the list/tuple length refers to the first
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[-1])
print(fruits[-3])


#Slicing tuples
#Range of Positive Indexes
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[:4])
print(fruits[0:])
print(fruits[1:3])

#Range of Negative Indexes
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[:-1])
print(fruits[-4:])
print(fruits[-3:-1])

#Changing Tuples to Lists
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)
fruits = tuple(fruits)
print(fruits)

#We can check if an item exists or not in a tuple using in, it returns a boolean.
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
print('apple' in fruits)
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

#We can join two or more tuples using + operator
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

#It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits