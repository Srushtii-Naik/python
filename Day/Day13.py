# #Filter only negative and zero in the list using list comprehension
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# negatives_and_zero = [ n for n in numbers if n <= 0]
# print(negatives_and_zero)

# #Flatten the following list of lists of lists to a one dimensional list :
# list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flatened_list = [num for sublist in list_of_lists for num in sublist]
# print(flatened_list)


# #Using list comprehension create the following list of tuples:
# 'List of tuples (powers)'
# tuple_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
# print(tuple_list)


#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened = [[country.upper(), country[:3].upper() , city.upper()] for sublist in countries for (country, city) in sublist]
print(flattened)

#Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list = [{'contry':country.upper(), 'city': city.upper()} for sublist in countries for (country, city) in sublist]
print(dict_list)

#Change the following list of lists to a list of concatenated strings:
names = [[('Srushti', 'Naik')], [('Sanjana', 'Naik')], [('Sandesh', 'A')], [('Ashok', 'Nayak')]]
full_names  = [f"{first} {last}" for sublist in names for (first,last) in sublist ]
print(full_names)

#Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2 : (y2 - y1 / x2 - x1)
intercept = lambda x,y,m : y - m*x
print(slope(2, 3, 5, 11)) 
print(intercept(2, 3, slope(2, 3, 5, 11)))