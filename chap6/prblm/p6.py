#cal grade

marks = int(input("Enter marks : "))
if (marks<=100 and marks >=90):
    print("Grade is: EX")
elif(marks<90 and marks>=80):
    print("Grade is: A")
elif(marks<80 and marks>=70):
    print("Grade is: B")
elif(marks<70 and marks>=60):
    print("Grade is: C")
elif(marks<60 and marks>50):
    print("Grade is: D")
elif(marks<=50):
    print("Grade is : F")
else:
    print("invalid num")
