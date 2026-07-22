#greatest num
a = int(input("enter num: "))
b = int(input("enter num: "))
c = int(input("enter num: "))
d = int(input("enter num: "))

if a>b and a>c and a>d:
    print("a is greater",a)
elif b>a and b>c and b>d:
    print("b is greater",b)
elif c>a and c>b and c>d:
    print("c is greater",c)
else:
    print("d is greater",d)


#greater num
a = int(input("enter num: "))
b = int(input("enter num: "))
c = int(input("enter num: "))
d = int(input("enter num: "))

greater = max(a,b,c,d)
print("greater is: ",greater)