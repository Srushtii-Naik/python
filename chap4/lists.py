# # A list is an ordered, mutable (changeable) collection that can store different types of data

# #Creating
family = ["Ashok","Savita","Sanjana","Sandesh"]
print(family)

# #indexing
print(family[0])
print(family[1])
print(family[3])
print(family[-2])


# #Slicing
print(family[:2])
print(family[-2:])

# #Updating List
family[2] = "Srushti"
print(family)

# #Adding Elements
print("append() ",family.append("Sanjana"))
print("insert()",family.insert(2,"Srushti"))
print("Adding Elements",family.extend(["Naik","xyz"]))

# # Removing Elements
print("remove()",family.remove("Srushti"))  #remove by name
print("pop()",family.pop(1))        #remove by index

# #Sorting
nums = [19,45,23,6,2,7,43,12]
nums.sort()
print("Sorting: ",nums)
#Descending
nums.sort(reverse=True)
print("Descending : ",nums)
#Reverse
nums.reverse()
print("Reverse: ",nums)

# #Useful Functions
t = [1,5,3,9,6,2,4]
print("len: ",len(t))
print("Max: ",max(t))
print("Min: ",min(t))
print("Sum: ",sum(t))


#List Comprehension (Very imp)
a = [1,2,3,4,5]
square = [x*x for x in a]
cube = [x*x*x for x in a]
print(square)
print(cube)
print("sum: ",sum(a))
print("Max: ",max(a))
print("Min: ",min(a))

#Nested List
matrix = [
    [1,2],
    [3,4]
]
print("Matrix is: ",matrix[1][0])



#Interview Questions
"List: Mutable"
"uses [] "
"more methods"
"used when data changes."


"Can a List contain Tuples? Yes."
"eg: data = [(1,2), (3,4), (5,6)]"