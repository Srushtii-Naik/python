#pass or not
a = int(input("Enter marks of sub1: "))
b = int(input("Enter marks of sub2: "))
c = int(input("Enter marks of sub3: "))
total_marks = (a+b+c)/300 * 100

if (total_marks >= 40 and a>=33 and b>=33 and c>=33):
    print("pass")
else:
    print("fail")