#Multiplication table of n in reverse order
n = int(input("Enter num: "))
for i in range(10, 0, -1):
    print(f"{n} X {i} = {i*n}")