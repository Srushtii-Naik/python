#name in list or not

lst = ["Srushti","Ashok","Savita","Sanjana","Sandesh"]
name  = input("Enter name: ")
if name in lst:
    print("Name is in list")
else:
    print("Name is not in list")


#another method
lst = ["Srushti","Ashok","Savita","Sanjana","Sandesh"]
name  = input("Enter name: ")
if name.capitalize() in lst:    #1st letter capital
    print("Name is in list")
else:
    print("Name is not in list")