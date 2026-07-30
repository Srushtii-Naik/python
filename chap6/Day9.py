
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


#Write a code which gives grade to students according to theirs scores:
score = int(input("Enter a score: "))
if score >= 90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("B")
elif score >=60:
    print("B")
else:
    print("F")

#Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("ENter month: ").capitalize()
if month in ["September","October","November"]:
    print("Season is Autumn")
elif month in ["December","January","February"]:
    print("Season is Winter")
elif month in ["March","April","May"]:
    print("Season is spring")
elif month in ["June","July","August"]:
    print("Season is Summer")
else:
    print("Invalid month entered")

#The following list contains some fruits . If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").lower()

if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print("Updated list:", fruits)