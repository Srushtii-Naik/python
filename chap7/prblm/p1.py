#multiplication table

a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))

for i in range(1, a+1):
    for j in range(1, b+1):
        print(i*j,end="\t")
    print()


# -----------------------------------------------------------------
n = int(input("Enter num: "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")