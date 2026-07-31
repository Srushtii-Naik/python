#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(n1,n2):
    sum = n1 + n2
    return sum
print(add_two_numbers(6,5))

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 3.14
    area = pi * r**2
    return area
print(area_of_circle(10))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for i in args:
        if isinstance(i,(int,float)):    # isinstance checks the type of 'i'
            total += i
        else:
            return f"Invalid input: {i} is not a numb"
    return total
print(add_all_nums(1, 2, 3.5))
print(add_all_nums(1, "hello", 3))

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(convert_celsius_to_fahrenheit(34))

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return "Autumn"
    elif month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['March','April','May']:
        return "Spring"
    else:
        return "Summer"
print(check_season("September"))

#Write a function called calculate_slope which return the slope of a linear equation
'Calculate slope (y2 - y1) / (x2 - x1)'
def calculate_slope(x1,y1,x2,y2):
    if x2 == x1:
        return "Slope is undefined (vertical line)"
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(2,3,4,5))


#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import math
def solve_quadratic_eqn(a,b,c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "no real solution"
    elif discriminant == 0:
        x = -b / (2*a)
        return [x]
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return [x1,x2]
print(solve_quadratic_eqn(5,4,3))

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list
def print_list(lst):
    for i in lst:
        print(i)
lst = [1, 2, 3, 4, 5]
print_list(lst)



#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops)
def reverse_list(arr):
    reverse_arr = []
    for i in range(len(arr)-1,-1,-1):
        reverse_arr.append(arr[i])
    return reverse_arr
print(reverse_list([1, 2, 3, 4, 5])) 

def reverse_list(arr):
    return arr[::-1]
print(reverse_list([1, 2, 3, 4, 5]))

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    capitalized = []
    for item in lst:
        if isinstance(item,str):
            capitalized.append(item.capitalize())
        else:
            capitalized.append(item)
    return capitalized
print(capitalize_list_items(["NaIk",'sRushti','ABX']))

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst,item):
    lst.append(item)
    return lst
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff,'Meat'))

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst,item):
    if item in lst:
        lst.remove(item)
    return lst
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff,'Mill'))

#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    total = 0
    for i in range(num+1):
        total += i
    return total
print(sum_of_numbers(5))

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range
def sum_of_odds(n):
    total = 0
    for i in range(1,n+1):
        if i%2 != 0:
            total += i
    return total
print(sum_of_odds(5))

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range
def sum_of_even(n):
    total = 0
    for i in range(1,n+1):
        if n%2 == 0:      #even
            total += i    # add the actual even number
    return total
print(sum_of_even(10))


# ___________________________________________________________________________________________________________________________________________________________________________________


#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number
def evens_and_odds(n):
    even = 0
    odd = 0
    for i in range(n+1):    # include n itself
        if i%2 == 0:
            even += 1       # count how many evens
        else:
            odd += 1        # count how many odds
    return f"The number of odds are {odd}.\nThe number of evens are {even}."
print(evens_and_odds(100))


#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact
print(factorial(5))


#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(check):
    if not check :
        return True
    return False
print(is_empty(0))


#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation)
import math
from collections import Counter

# Mean (Average)
def calculate_mean(lst):
    # Formula: mean = sum of all numbers / count of numbers
    total = sum(lst)          # add all numbers
    count = len(lst)          # how many numbers
    return total / count      # divide → average


# Median (Middle value)
def calculate_median(lst):
    sorted_lst = sorted(lst)  # step 1: sort the list
    n = len(sorted_lst)       # step 2: count numbers
    mid = n // 2              # step 3: find middle index

    # Formula:
    # if odd → middle value
    # if even → average of two middle values
    if n % 2 == 0:            # even count
        return (sorted_lst[mid-1] + sorted_lst[mid]) / 2
    else:                     # odd count
        return sorted_lst[mid]


# Mode (Most frequent value)
def calculate_mode(lst):
    counts = Counter(lst)     # step 1: count frequency of each number
    max_count = max(counts.values())  # step 2: find highest frequency
    modes = [k for k, v in counts.items() if v == max_count]

    # Formula: mode = value(s) with max frequency
    if len(modes) == 1:
        return modes[0]       # only one mode
    return modes              # multiple modes possible


# Range (Max - Min)
def calculate_range(lst):
    # Formula: range = largest - smallest
    return max(lst) - min(lst)


# Variance (Spread of data)
def calculate_variance(lst):
    mean = calculate_mean(lst)   # step 1: find mean
    # Formula: variance = average of (x - mean)^2
    differences = [(x - mean) ** 2 for x in lst]  # step 2: square differences
    return sum(differences) / len(lst)            # step 3: average them


# Standard Deviation (Square root of variance)
def calculate_std(lst):
    # Formula: std = sqrt(variance)
    return math.sqrt(calculate_variance(lst))


#Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name
def greet(name='Guest'):
    return f"Hello, {name}!"
print(greet())
print(greet("Srushti"))

def show_args(**kwargs):
    # kwargs is a dictionary of all named arguments
    result = "Received: "
    pairs = []
    for key, value in kwargs.items():
        pairs.append(f"{key}: {value}")   # format each as "name: value"
    result += ", ".join(pairs)            # join them with commas
    print(result)


show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York

show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny
