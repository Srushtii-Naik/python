# Calculating area of a circle
radius = int(input("Enter radius :  "))
area_circle = 3.14 * radius**2     # two * sign means exponent or power
print("Area of a circle : ",area_circle)

# Calculating area of a rectangle
len = int(input("Enter length :  "))
width = int(input("Enter width :  "))
area_rect = len * width
print("Area of a Rectangle : ",area_rect)

# Calculating area of a triangle
base = int(input("Enter base  :  "))
height = int(input("Enter height :  "))
area_tri = 0.5 * base * height
print("Area of a triangle : ",area_tri)

# Calculating a weight of an object
gravity = 9.81
mass = int(input("Enter mass of obj: "))
weight = mass * gravity
print(f"Weight of mass: {weight} N")

# Calculate the density of a liquid
mass = 75
vol = 0.075
density = mass / vol
print(density,'Kg/m^3')

