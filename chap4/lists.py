# # # A list is an ordered, mutable (changeable) collection that can store different types of data

# # #Creating
# family = ["Ashok","Savita","Sanjana","Sandesh"]
# print(family)

# # #indexing
# print(family[0])
# print(family[1])
# print(family[3])
# print(family[-2])


# #Unpacking List Items
# lst = ['item1','item2','item3', 'item4', 'item5']
# first_item, second_item, third_item, *rest = lst
# print(first_item)     # item1
# print(second_item)    # item2
# print(third_item)     # item3
# print(rest)           # ['item4', 'item5']
# # Second Example about unpacking list
# first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
# print(first)          # 1
# print(second)         # 2
# print(third)          # 3
# print(rest)           # [4,5,6,7,8,9]
# print(tenth)          # 10


# # #Slicing
# print(family[:2])
# print(family[-2:])

# # #Updating List
# family[2] = "Srushti"
# print(family)

# # #Adding Elements
# print("append() ",family.append("Sanjana"))
# print("insert()",family.insert(2,"Srushti"))
# print("Adding Elements",family.extend(["Naik","xyz"]))

# # # Removing Elements
# print("remove()",family.remove("Srushti"))  #remove by name
# print("pop()",family.pop(1))        #remove by index

# # #Sorting
# nums = [19,45,23,6,2,7,43,12]
# nums.sort()
# print("Sorting: ",nums)
# #Descending
# nums.sort(reverse=True)
# print("Descending : ",nums)
# #Reverse
# nums.reverse()
# print("Reverse: ",nums)

# # #Useful Functions
# t = [1,5,3,9,6,2,4]
# print("len: ",len(t))
# print("Max: ",max(t))
# print("Min: ",min(t))
# print("Sum: ",sum(t))


# #List Comprehension (Very imp)
# a = [1,2,3,4,5]
# square = [x*x for x in a]
# cube = [x*x*x for x in a]
# print(square)
# print(cube)
# print("sum: ",sum(a))
# print("Max: ",max(a))
# print("Min: ",min(a))

# #Nested List
# matrix = [
#     [1,2],
#     [3,4]
# ]
# print("Matrix is: ",matrix[1][0])



# #Interview Questions
# "List: Mutable"
# "uses [] "
# "more methods"
# "used when data changes."


# "Can a List contain Tuples? Yes."
# "eg: data = [(1,2), (3,4), (5,6)]"

# ___________________________________________________________________________________________________________________________________________________________________________________




# #List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits[0] = 'avocado'
# print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
# fruits[1] = 'apple'
# print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
# last_index = len(fruits) - 1
# fruits[last_index] = 'lime'
# print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']


# #Checking an item if it is a member of a list using in operator.
# fruits = ['banana', 'orange', 'mango', 'lemon']
# does_exit = 'banana' in fruits
# print(does_exit)    #True
# does_exit = 'lime' in fruits
# print(does_exit)    #False


# #To add item to the end of an existing list we use the method append().
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.append('apple')
# print(fruits)

# #We can use insert() method to insert a single item at a specified index in a list.
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.insert(2,'apple')
# print(fruits)


# #The remove method removes a specified item from a list
# fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
# fruits.remove('lemon')
# print(fruits)

# #The pop() method removes the specified index, (or the last item if index is not specified)
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.pop()
# print(fruits)
# fruits.pop(2)
# print(fruits)

# #The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely
# fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
# del fruits[0]
# print(fruits)
# del fruits[1:3]
# print(fruits)
# del fruits
# print(fruits)   # This should give: NameError: name 'fruits' is not defined

# #The clear() method empties the list
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.clear()
# print(fruits)

# #Copying a List: It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits_copy = fruits.copy()
# print(fruits_copy)

# #Joining Lists:  There are several ways to join, or concatenate, two or more lists in Python.
# fruits = ['banana', 'orange', 'mango', 'lemon']
# vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)

# #The extend() method allows to append list in a list
# fruits = ['banana', 'orange', 'mango', 'lemon']
# vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
# fruits.extend(vegetables)
# print(fruits)

# #Counting Items in a List:  The count() method returns the number of times an item appears in a list
# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(fruits.count('orange'))
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# print(ages.count(24))

#Finding Index of an Item: The index() method returns the index of an item in the list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

#Reversing a List: The reverse() method reverses the order of a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages[::-1])

#Sorting List Items: To sort lists we can use sort() method or sorted() built-in functions

#sort(): this method modifies the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

#sorted(): returns the ordered list without modifying the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))
fruits = sorted(fruits,reverse=True)
print(sorted(fruits))