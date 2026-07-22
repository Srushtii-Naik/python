#factorial of num
n = int(input("Enter num: "))
fact  = 1           #multi = always startwith 1
for i in range(1, n+1):
    fact = fact * i
print(f"Factorial of {n} is = {fact}")