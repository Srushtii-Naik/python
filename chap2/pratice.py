age = 20    #Declare your age as integer variable
height = 6.5('in foot')   #Declare your height as a float variable
comp = (3 +4j) #Declare a variable that store a complex number


# 'Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)'
a = int(input("enter side a: "))
b = int(input("enter side b: "))
c = int(input("enter side c: "))
perimeter = a+b+c
print("perimeter of triangle: ",perimeter)



# 'Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))'
len = int(input("Enter len: "))
width = int(input("Enter width: "))
area = len * width
perimeter = 2 * (len + width)
print(f"Area of Rectangle : {area}")
print(f"Perimeter of Rectangle : {perimeter}")



# 'Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14'
radius = int(input("Enter radius of circle: "))
area_circle = 3.14 * radius**2
circumference = 2 * 3.14 * radius
print(f"Area of Circle: {area_circle}")
print(f"Circumference of Circle: {circumference}")



# 'Calculate the slope, x-intercept and y-intercept of y = 2x -2'
# Equation: y = 2x - 2
slope = 2           # slope is the coefficient of x
y_intercept = -2    # y-intercept is the constant term (when x = 0)
x_intercept = 1     # x-intercept is when y = 0  # 0 = 2x - 2  =>  2x = 2  =>  x = 1
print("Slope:", slope)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)



# 'Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)'
import math
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)   # Slope
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)   # Euclidean distance
print("Slope:", slope)
print("Euclidean Distance:", distance)



# 'Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0'
for x in [-5,-4,-3,-2,-1,0,1]:
    y = x**2 + 6*x + 9
    print(f"x={x}, y={y}")
root = -3
print("Root (x where y=0):", root)



# 'Find the length of python and dragon and make a falsy comparison statement'

if len("python") != len("dragon"):
    print(True)
else:
    print(False)



# 'Use and operator to check if ''on'' is found in both ''python'' and ''dragon'' '
if "on" in "python" and "on"in "dragon":
    print(True)



# 'I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence'
line = "I hope this course is not full of jargon"
if "jargon" in line:
    print(f"found ")


#Find the length of the text python and convert the value to float and convert it to string
word = "python"
length = len(word)
length_float = float(length)
length_string = str(length)    #or length_string = str(float_length)
print("Length:", length)
print("As float:", length_float)
print("As string:", length_string)


#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
n = int(input("enter num: "))
if n%2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is not even")


#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_div = 7//3
int_val = int(2.7)  # convert 2.7 to integer (2)
print(floor_div == int_val)


#Check if type of '10' is equal to type of 10
print(type(10))
print(type('10'))
print(type('10') == type(10))


#Check if int('9.8') is equal to 10
print(type('9.8') == type(10))


#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hr = int(input("Enter hour: "))
rph = int(input("Enter rate per hour: "))
print(hr * rph)


#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
year = int(input("Enter num of year : "))
sec = 365 * 24 * 60 * 60 
print(f"You have lived for {year * sec} sec")

#Write a Python script that displays the following table
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
print('1 1 1 1 1')
for i in range(2,6):
    print(i, 1, i, i**2, i**3)