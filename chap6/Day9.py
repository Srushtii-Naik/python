
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years
age = int(input("enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive")
else:
    req_age = 18 - age
    print(f"you need {req_age} more year")

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age
my_age = 20
your_age = int(input("Enter your age: "))
if my_age == your_age:
    print("We are same age!")
elif my_age > your_age:
    diff = my_age - your_age
    print(f"i am  {diff} year older than you ")
else:
    diff = your_age - my_age
    print(f"you are  {diff} year older than me ")

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b
a = int(input("Enter a num: "))
b = int(input("Enter b num: "))
if a > b :
    print("a is greater than b")
elif a < b:
    print("a is smaller than b,")
else:
    print("a is equal to b")
