# #Declare an empty list
# lst = []

# #Declare a list with more than 5 items
# lst = ['A',23,'Srushti',65.89,'CSE']

# #Find the length of your list
# print(len(lst))

# #Get the first item, the middle item and the last item of the list
# lst = ['A',23,'Srushti',65.89,'CSE']
# print(lst[0])
# mid = len(lst) // 2
# print(lst[mid])
# print(lst[-1])

# #Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
# mixed_data_types = ['Srushti',20,'5.8','None','Banglore']
# print(mixed_data_types)

# #Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# print(it_companies)

# #Print the number of companies in the list
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# print(len(it_companies))

# #Print the first, middle and last company
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# print(it_companies[0])
# mid = len(it_companies)//2
# print(it_companies[mid])
# print(it_companies[-1])

# #it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# it_companies.append('MindMesh')
# print(it_companies)

# #Add an IT company to it_companies
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# it_companies.append('Infosys')
# print(it_companies)

# #Insert an IT company in the middle of the companies list
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# mid = len(it_companies)//2
# it_companies.insert(mid,"TCS")
# print(it_companies)

# #Change one of the it_companies names to uppercase (IBM excluded!)
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# it_companies[1] = it_companies[1].upper()
# print(it_companies)

# #Join the it_companies with a string '#;  '
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# joined = '#; '.join(it_companies)
# print(joined)

# #Check if a certain company exists in the it_companies list.
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# print('Google' in it_companies)

# #Sort the list using sort() method
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# print(it_companies.sort())
# print(it_companies)

# #Reverse the list in descending order using reverse() method
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# it_companies.sort(reverse=True)
# print(it_companies)

# #Slice out the first 3 companies from the list
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# print(it_companies[:3])

# #Slice out the last 3 companies from the list
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# print(it_companies[-3:])

# #Slice out the middle IT company or companies from the list
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# leng = len(it_companies)
# mid = leng // 2
# if leng%2 != 0:
#     middle = it_companies[mid]
# else: 
#     middle = it_companies[mid-1:mid+1]
# print(middle)

# #Remove the first IT company from the list
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
# it_companies.remove('Facebook')
# print(it_companies)
# del it_companies[0]
# print(it_companies)

#Remove the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
leng = len(it_companies)
mid = leng // 2
if leng%2 != 0:
    it_companies.pop(mid)
else:
    it_companies.pop(mid)
    it_companies.pop(mid-1)
print(it_companies)

#Remove the last IT company from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
it_companies.pop()
print(it_companies)

#Remove all IT companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
it_companies.clear()
print(it_companies)

#Destroy the IT companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
del it_companies

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
res = front_end + back_end
print(res)

front_end.extend(back_end)
print(res)


#Join the following lists: After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined = front_end + back_end
full_stack = joined.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)
