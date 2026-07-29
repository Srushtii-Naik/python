# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['Infosys','TCS','Wipro'])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Oracle')
print(it_companies)

#What is the difference between remove and discard
# remove() → raises an error if the element is not found
# discard() → does nothing if the element is not found
it_companies.discard('Nonexistance')
print(it_companies)



A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


print(A.union(B))               #Join A and B
print(A.intersection(B))        #Find A intersection B
print(A.issubset(B))            #Is A subset of B
print(A.isdisjoint(B))          #Are A and B disjoint sets
print(A.union(B),B.union(A))    #Join A with B and B with A
print(A.symmetric_difference(B)) #What is the symmetric difference between A and B
del A, B                         #Delete the sets completely



#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print(len(age))     #8 (because duplicates are counted)
print(len(age_set)) #5 (because sets remove duplicates)


#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)  
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))

#Explain the difference between the following data types: string, list, tuple and set
# String: sequence of characters, immutable
s = "Hello"
print(s[0])          # 'H'
# s[0] = 'h'         # ❌ Error (strings cannot be changed)

# List: ordered collection, allows duplicates, mutable
my_list = [1, 2, 3, 2]
print(my_list[0])     # 1
my_list[0] = 10       # ✅ can modify
print(my_list)        # [10, 2, 3, 2]

# Tuple: ordered collection, allows duplicates, immutable
my_tuple = (1, 2, 3, 2)
print(my_tuple[0])    # 1
# my_tuple[0] = 10    # ❌ Error (tuples cannot be changed)

# Set: unordered collection, no duplicates, mutable
my_set = {1, 2, 3, 2}
print(my_set)         # {1, 2, 3} (duplicates removed)
my_set.add(4)         # ✅ can add new elements
print(my_set)         # {1, 2, 3, 4}
