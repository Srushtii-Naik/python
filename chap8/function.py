#function
'block of reuseable code tht performs specific task'

def greet(name):
    print(f"Hello! {name}")
greet("Srushti")

#multiple parameter
def add(a,b):
    print(a+b)
add(10,20)

#return statement 'sends a value back to the caller'
def square(n):
    return n*n
res = square(5)
print(res)

# -------------------------------------------------------------------------------------------------------------------
#Difference Between print() and return()
def fun1():
    print(5)        #only displays the value.

def fun2():
    return 5        #sends the value back so it can be stored or used later.

print(fun1())
print(fun2())

# ---------------------------------------------------------------------------------------------------------------------
#types of function
'Built-in function --------Already provided by Python'
def bulit(a,b):
    len(a)
    max(a,b)
    min(a,b)
    sum(a,b)
    type(a,b)
    print(a,b)
    input()
bulit(2,3)

'user-def -------------created by the programmer'
def greet(name):
    print(f"Hello! {name}")
greet("Srushti")

# ---------------------------------------------------------------------------------------------------------
'Default Arguments--------If no value is passed, the default value is used'
def greet(name="Guest"):
    print(f"Hello! {name}")
greet()
greet("Srushti")

'Keyword Arguments-----order doesnt matter because arguments are passed by name'
def student(name,age):
    print(name, ":",age)
# student(age=20,name="srushti")

'Variable-Length Arguments (*args)------num of arguments is unknown'
def sums(*num):
    print(sum(num))
sums(10,20)
sums(10,20,30,40)

'Keyword Variable Arguments (**kwargs)----Accepts any num of keyword arguments.'
def info(**data):
    print(data)
info(name="Srushti,age=20")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
'Scope of Variables'

#local var      "Exists only inside the function"
def demo():
    x = 10
    print(x)
demo()

#global var     "Accessible throughout the program"
x = 100
def show():
    print(x)
show()

# ---------------------------------------------------------------------------------------------------------------------------------------------------
'Lambda(Anonymous) function --------small fun written in 1 line'
square = lambda x: x*x
print(square(5)) 
