#Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)

i=0
while i <= 10:
    print(i)
    i = i+1


#Iterate 10 to 0 using for loop, do the same using while loop
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i = i-1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle
for i in range(1,8):
    print(i * "#")


#Use nested loops to create the following
for i in range(1,8):
    for j in range(1,8):
        print("*",end=' ')
    print()

#Print the following pattern: Tables
for i in range(11):
    print(f"{i} X {i} = {i*i}")


#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for item in lst:
    print(item)

#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i%2 == 0:
        print(i)

#Use for loop to iterate from 0 to 100 and print only odd numbers\
for i in range(101):
    if i%2 != 0:
        print(i)
