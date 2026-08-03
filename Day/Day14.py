'Higher Order Functions'

#Function as a Parameter
def sum_num(n):     # normal function
    return sum(n)   # a sad function abusing the built-in sum function :<

def higher_order_fun(f, lst):
    summation = f(lst)
    return summation
result = higher_order_fun(sum_num, [1,2,3,4,5])
print(result)


#Function as a Return Value
def square(x):
    return x*x
def cube(x):
    return x**3
def absoulte(x):
    if x >= 0:
        return x
    else: 
        return -(x)
def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absoulte':
        return absoulte
result = higher_order_function('square')
print(result(3))
result = higher_order_function('cube')
print(result(3)) 
result = higher_order_function('absoulte')
print(result(-3))

# ___________________________________________________________________________________________________________________________________________________________________________________


#Python Closures
'remembers the variables from its outer function even after the outer function has finished executing'

def add_ten():
    ten = 10
    def add(num):
        return num + 10
    return add
closure_result = add_ten()
print(closure_result(5))


#adds extra functionality to another function without modifying its original code
# Normal function
def greeting():
    return 'welcome to python!'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())


#Python Decorators


# ___________________________________________________________________________________________________________________________________________________________________________________



'Built-in Higher Order Functions'


#map() function is a built-in function that takes a function and iterable as parameters.
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x**2
num_square = map(square,numbers)
print(list(num_square))
# Lets apply it with a lambda function
num_square = map(lambda x: x**2, numbers)
print(list(num_square))


numbers_str = ['1', '2', '3', '4', '5'] 
num_int = map(int, numbers_str)
print(list(num_int))


names = ['Srushti', 'sanjana', 'Sandesh', 'Savita','ashok']
def change_upper(name):
    return name.upper()
names_upper = map(change_upper, names)
print(list(names_upper))


# ___________________________________________________________________________________________________________________________________________________________________________________

'filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria'
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]
def even_num(n):
    if n%2 == 0:
        return True
    return False
even_numbers = filter(even_num,numbers)
print(list(even_numbers))


numbers = [1, 2, 3, 4, 5] 
def odd_num(n):
    if n%2 != 0:
        return True
    return False
odd_numers = filter(odd_num, numbers)
print(list(odd_numers))

# Filter long name

names = ['Srushti', 'sanjana', 'Sandesh', 'Savita','ashok']
def is_name_long(name):
    if len(name) > 7:
        return True
    return False
long_name = filter(is_name_long, names)
print(list(long_name))