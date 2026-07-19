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