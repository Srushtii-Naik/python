
'A module is a file containing a set of codes or a set of functions which can be included to an application'
'Instead of writing the same code again and again, you can put it in a module and import it whenever needed'


#Importing a Module: To import the file we use the import keyword and the name of the file only
'''
'Built-in Modules : These modules come pre-installed with Python'
Module     = Purpose
math	   = Mathematical functions
random	   = Random numbers
os	       = Operating system operations
sys	Python = interpreter information
datetime   = Date and time
statistics = Statistical calculations
'''



'''
Third-Party Modules
These are created by other developers and are not included with Python.They must be installed using pip.
    numpy
    pandas
    matplotlib
    requests
    flask
    django

'''


import mymodule
print(mymodule.full_name('Srushti','Naik'))


#We can have many functions in a file and we can import all the functions differently.
from mymodule import full_name , sum_num , person , gravity
print(full_name('Srushti','Naik'))
print(sum_num(5))

mass = 100
weight = mass * gravity
print(weight)

print(person['skills'])



#During importing we can rename the name of the module
from mymodule import full_name as name , sum_num as total , person as me , gravity as g
print(name('Srushti','Naik'))
print(total(5))
print(100 * g)
print(me)
print(me['age'])


# ___________________________________________________________________________________________________________________________________________________________________________________



'Import Built-in Modules'


#OS Module
import os               # import the module
os.mkdir('SrushtiNaik') # Creating a directory
os.chdir('')            # Changing the current directory
os.getcwd()             # Getting current working directory
os.rmdir('SrushtiNaik') # Removing directory


#Sys Module
import sys 
# print('Welcome {} . Enjoy {} programming!'.format(sys.argv[1],sys.argv[2]))
# sys.exit()
print(sys.maxsize)  # To know the largest integer variable it takes(2**63 - 1)[64bit]
print(sys.version)  # To know the version of python you are using
print(sys.path)     # To know environment path
sys.exit()          # to exit sys


#Statistics Module
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

#Math Module
import math 
print(dir(math)) #Shows everything available inside a module.
print(math.pi)
print(math.sqrt(5))
print(math.pow(2,3))
print(math.floor(9.81)) # 9, rounding to the lowest
print(math.ceil(9.81))  # 10, rounding to the highest
print(math.log10(100))
print(math.e)
print(math.factorial(5))
print(math.gcd(5,6))
print(math.lcm(5,6))
help(math)

#It is also possible to import multiple functions at once
from math import pi, sqrt ,pow, floor , ceil 
from math import *
print(pi)
print(sqrt(5))
print(pow(2,3))

#When we import we can also rename the name of the function.
from math import pi as PI
print(PI)


#String module
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

#Random Module
import random
print(random.random())
print(random.choice(['apple', 'banana', 'cherry']))
print(random.choices([1, 2, 3, 4, 5]))
print(random.randint(1,50))


