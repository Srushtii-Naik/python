'Recursion --------function calling itself'
#A recursive function must have a "Base Case"(stopping condition that prevents infinite recursion)

#num 1-5
def num(n):
    if n == 6:
        return
    print(n)
    num(n+1)
num(1)

#factorial
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)
print(fact(5))

#fibonacci 
def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(6))





# ------------------------------------------------------------------------------------------------------------------
'INTERVIEW '

'Difference between parameter and argument?'
def greet(name):     #name = parameter(var in fun defination)
    print(name)
greet("srushti")     #srushti = argument(actual val passed dur fun call)