
#Built in functions
def demo():
    print("abs: ",abs(-10))             # absolute value
    print("Max: ",max([1,2,6,5]))       # largest
    print("Min: ",min([5,3,7,1]))       # smallest
    print("Len: ",len([1,5,2]))         # length
    print("Sum: ",sum([1,6,5,8,9]))     # total
    print("Round: ",round(3.14159,2))   # round off
    print("Sorted: ",sorted([9,5,6,8])) # sort list
    print("type: ",type("python"))      # type of object
    print("str:",str(123))              # convert to string
    print("int:",int("65"))             # convert to int
    print("float:",float("65"))         # convert to float
    print("list:",list("abc"))          # convert to list
    print("tuples:",tuple([1,2,3]))     # convert to tuple
    print("Set",set([1,2,2,3,4,6,5]))   # convert to set
    print("Zip",list(zip([1,2],[6,5]))) # combine lists
demo()

# ___________________________________________________________________________________________________________________________________________________________________________________

#Python keywords---Keywords are reserved words in Python, cannot use them as variable 
'''
conditional : 
    if → conditional check 
    elif  → extra condition after if
    else → run if no condition true

loop: 
    for → loop through items
    while → loop until condition false
    break → exit loop early 
    continue → skip to next loop step 
    in → check membership in sequence

function: 
    def → define a function
    return → send value back from function
    lambda → small anonymous function
    yeild → return value from generator

Classes/Objects: 
    class → define a class
    self → reference current object in class
    super → call parent class methods
    __init__ → Used to initialize data when object is created(Constructor)

import : 
    import → bring in a module
    from → import specific part of module
    as → give alias name to module

exceptions: 
    try  → start error handling block
    except → handle specific error
    finally → always run cleanup code
    raise → throw an error manually

boolean/null : 
    True → boolean true value
    False → boolean false value
    None → empty / no value

logic: 
    and → logical AND 
    or → logical OR
    not → logical NOT
    is → check identity (same object)

scope: 
    global → use global variable inside function 
    nonlocal → use outer function variable

context: 
    with → simplify resource handling (like files)
    assert → check condition, raise error if false
    del → delete variable or object
    pass → do nothing (placeholder)
'''
# ___________________________________________________________________________________________________________________________________________________________________________________

# Demo program showing Python keywords

# global keyword
x = 10
def use_global():
    global x
    x = 20
use_global()
print("global:", x)

# def, return, lambda
def square(n): return n*n
print("def+return:", square(5))
add = lambda a,b: a+b
print("lambda:", add(2,3))

# class, self, __init__, super
class Parent:
    def greet(self): return "Hello from Parent"
class Child(Parent):
    def __init__(self, name): self.name = name
    def greet(self): return super().greet() + " & Child"
c = Child("Srushti")
print("class+super:", c.greet())

# if, elif, else
n = -1
if n > 0: print("Positive")
elif n == 0: print("Zero")
else: print("Negative")

# for, in, range
for i in range(3): print("for:", i)

# while, break, continue
i = 0
while i < 5:
    i += 1
    if i == 2: continue
    if i == 4: break
    print("while:", i)

# try, except, finally, raise
try:
    raise ValueError("Oops!")
except ValueError as e:
    print("except:", e)
finally:
    print("finally: always runs")

# with (file handling)
with open("demo.txt", "w") as f:
    f.write("Hello file")
print("with: file written")

# assert
assert 2+2 == 4, "Math broken!"
print("assert: passed")

# yield (generator)
def gen():
    yield 1
    yield 2
for val in gen(): print("yield:", val)

# del
a = [1,2,3]
del a[0]
print("del:", a)

# pass
for i in range(2):
    pass  # placeholder
print("pass: loop skipped")

# True, False, None
print(True, False, None)

# and, or, not, is
print("logic:", (True and False), (True or False), (not True))
print("is:", c is c)

# nonlocal
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "changed"
    inner()
    return x
print("nonlocal:", outer())
