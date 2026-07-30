#Star pattern (n = 3)

n = int(input("enter num: "))
for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*i-1))


n = int(input("enter num: "))
for i in range(1,n+1):
    space = " " * (i-1)     
    star = "*"*(2*i - i)    # odd number of stars
    print(space + star)