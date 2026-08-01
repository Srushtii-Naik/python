
'List Comprehension:  It is a short way to create a new list'


#change a string to a list of characters
language = 'Python'
lst = list(language)
print(lst)
# Second way: list comprehension
language = 'Python'
lst = [i for i in language]
print(lst)


#generate a list of numbers
numb = [i for i in range(10)]
print(numb)
# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)
# It is also possible to make a list of tuples
numbers = [(i,i*i) for i in range(11)]
print(numbers)


'List comprehension can be combined with if expression'

# Generating even numbers
even = [ i for i in range(21) if i%2 == 0]
print(even)
# Generating odd numbers
odd = [ i for i in range(21) if i%2 != 0]
print(odd)

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive = [ i for i in numbers if i>0]
negetive = [ i for i in numbers if i<0]
positive_even = [ i for i in numbers if i%2 == 0 and i>0]
print(positive_even)
print(positive)
print(negetive)

# Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattend_list = [number for row in list_of_lists for number in row]
print(flattend_list)


# ___________________________________________________________________________________________________________________________________________________________________________________


'Lambda Function'

# Named function
def add_two_num(a,b):
    return a+b
print(add_two_num(2,3))
# Lets change the above function to a lambda function
add_two_num = lambda a,b : a+b
print(add_two_num(5,6))


# Self invoking lambda function
(lambda a,b : a+b)(2,3)

square = lambda x : x**2
print(square(4))

cube = lambda x: x**3
print(cube(6))

multiple_variable = lambda a,b,c : a**2 -3*b + 4*c
print(multiple_variable(5,5,3))


#Using a lambda function inside another function.
def power(x):
    return lambda n: x**n
cube = power(2)(3)      # function power now need 2 arguments to run, in separate rounded brackets
print(cube)
two_power_of_five = power(2)(5)
print(two_power_of_five)