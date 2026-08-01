#Creating a Module: To create a module we write our codes in a python script and we save it as a .py file
def full_name(firstname,lastname):
    return firstname + " " + lastname

def sum_num(n):
    sum = 0
    for i in range(n+1):
        sum = sum+i
    return sum

person ={
    'name':"Srushti",
    'age':20,
    'branch':'CSE',
    'CGPA':'9',
    'Clg':"DSATM",
    'girl':True,
    'skills':["HTML","CSS","Python","github"],
    'address': {'country': 'india', "city":" bnglr", "pincode":560021}
}

gravity = 9.81