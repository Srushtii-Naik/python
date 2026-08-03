#Packing and Unpacking Arguments in Python
'Packing means collecting multiple values into a single variable'
#We use two operators: ( * )for tuples   ( ** ) for dictionaries


#Packing Lists
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,6,7))

def add(*num):
    print(type(num))    #Python packs them into a tuple
    print(num)
add(1,2,3,4)

#Packing Dictionaries
def packing_person_info(**kwargs):  #**kwargs collects multiple keyword arguments into a dictionary
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs
print(packing_person_info(name = 'Srushti', country = 'India', city = 'Banglore', age =20))


def student(**details):
    print(details['name'])
    print(details['age'])
student(name='Srushti',age=20)

# ___________________________________________________________________________________________________________________________________________________________________________________

'Unpacking means extracting values from a collection (list, tuple, dictionary) into separate variables'

#Unpacking a Tuple
numbers = (10,20,30)
a,b,c = numbers
print(a)
print(b)
print(c)

#Unpacking a List
fruits = ["Apple", "Mango", "Orange"]
a,b,c = fruits
print(a)
print(b)
print(c)


#Using * in Unpacking:  The * operator collects the remaining values
numbers = [1, 2, 3, 4, 5]
a, *b = numbers
print(a)
print(b)



def sum_5_num(a,b,c,d,e):
    return a+b+c+d+e
lst = [1,2,3,4,5]
# print(sum_5_num(lst))
#When we run the this code, it raises an error, because this function takes numbers (not a list) as arguments. Let us unpack/destructure the list
def sum_5_num(a,b,c,d,e):
    return a+b+c+d+e
lst = [1,2,3,4,5]
print(sum_5_num(*lst))

#We can also use unpacking in the range built-in function that expects a start and an end
number = range(2,7)
print(list(number))
args = [2,7]
number = range(*args)
print(number)


#A list or a tuple can also be unpacked like this:
numbers = [1, 2, 3, 4, 5, 6, 7]
first , *middle , last = numbers
print(first, middle, last)

#Unpacking Dictionaries
def unpacking_person_info(name,country, city, age):
    return f'{name} lives in {country},{city} . she is {age} year old'
dct = {'name':'Srushti','country':'India','city':'Banglore','age':20}
print(unpacking_person_info(**dct))

# ___________________________________________________________________________________________________________________________________________________________________________________


#Spreading in Python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)
parent = ['Ashok','Savitha']
childrens = ['Srushti','Sanjana','Sandesh']
family = [*parent, *childrens, 'Naik']
print(family)

#If we are interested in an index of a list, we use enumerate built-in function to get the index of each item in the list
for index, item in enumerate([20,30,40]):
    print(index,item)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland','India']
for index, i in enumerate(countries):
    if i == 'India':
        print(f'The country {i} has been found at index {index}')


# ___________________________________________________________________________________________________________________________________________________________________________________

#Zip: Sometimes we would like to combine lists when looping through them
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits,vegetables):
    fruits_and_veges.append({'Fruit':f, 'Veg':v})
print(fruits_and_veges)