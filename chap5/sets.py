# #Creating an empty set
# s = set()      #Empty curly brackets {} will create a dictionary

# #Creating a set with initial items
# fruits = {'banana', 'orange', 'mango', 'lemon'}

# #We use len() method to find the length of a set.
# print(len(fruits))

# #Accessing Items in a Set: We use loops to access items

# #To check if an item exist in a list we use in membership operator.
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# print('orange' in fruits)

# #Add one item using add()
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.add('lime')
# print(fruits)

# #Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.update(['apple','kiwi','watermelon'])
# print(fruits)

# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
# fruits.update(vegetables)
# print(fruits)

# #The pop() methods remove a random item from a list and it returns the removed item.
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.pop()    # removes a random item from the set

# #If we want to clear or empty the set we use clear method.
# fruits.clear()
# print(fruits)

# #f we want to delete the set itself we use del operator.
# del s
# del fruits

# #We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.
# fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
# fruits = set(fruits)
# print(fruits)

# #We can join two sets using the union() or update() method or | symbol 
# #Union This method returns a new set
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
# print(fruits.union(vegetables))
# print(fruits | vegetables)

# #Update This method inserts a set into a given set
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
# fruits.update(vegetables)
# print(fruits)

#Intersection returns a set of items which are in both the sets or using & symbol. See the example
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))

#A set can be a subset or super set of other sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers))     # False, because it is a super set
print(whole_numbers.issuperset(even_numbers))   #True
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

#Checking the Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))
python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)
print(dragon.difference(python))

#Finding Symmetric Difference Between Two Sets --> keeps only the non‑common elements.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers)) #“exclusive OR” for sets.
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.symmetric_difference(dragon))

#We can check if two sets are joint or disjoint using isdisjoint() method.
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))  # True, because no common item
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))    ## False, there are common items {'o', 'n'}