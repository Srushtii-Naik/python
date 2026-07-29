# #Create an empty tuple
# t = ()

# #Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# sis = ('Sanjana','Arathi')
# bro = ('Sandesh','Prasanth')

# #Join brothers and sisters tuples and assign it to siblings
# sibling = sis + bro
# print(sibling)

# #How many siblings do you have?
# print(len(sibling))

# #Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# family_members = sibling + ("Ashok","Savita")
# print(family_members)


# #Unpack siblings and parents from family_members
# siblings = family_members[:-2]      # all except last two
# parents = family_members[-2:]
# print("Siblings:", siblings)
# print("Parents:", parents)


# ___________________________________________________________________________________________________________________________________________________________________________________

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "banana", "mango", "orange")
vegetables = ("carrot", "potato", "spinach", "onion")
animal_products = ("milk", "egg", "cheese", "meat")
food_stuff_tp = fruits + vegetables + animal_products
# print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# print(food_stuff_lt)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
n = len(food_stuff_lt)
mid = n // 2
if n%2 == 0:
    middle = food_stuff_lt[mid-1:mid+1]
else:
    middle = food_stuff_lt[mid]
print(middle)

#Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

#Delete the food_stuff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
# print(food_stuff_tp)


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)
#Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
