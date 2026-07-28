#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
s1 = 'Thirsty'
s2 = 'Days'
s3 = 'of'
s4 = 'Python'
res = s1 + s2+ s3+ s4
print(res)
 #or
word = ['Thirty', 'Days', 'Of', 'Python']
res = ' '.join(word)
print(res)


#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
s1 = 'coding'
s2 = 'for'
s3 = 'all'
print(f"{s1} {s2} {s3}")

# ___________________________________________________________________________________________________________________________________________________________________________________


#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print()
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
challenge = "Coding For All"
res = challenge.split()[1:]
print(res)

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
challenge = "Coding For All"
print(challenge.find("Coding"))
print(challenge.index("Coding"))
print("Coding" in challenge)

#Replace the word coding in the string 'Coding For All' to Python.
challenge = "Coding For All"
print(challenge.replace("Coding","Python"))

#Change "Python for Everyone" to "Python for All" using the replace method or other methods.
challenge1 = "Python for Everyone"
print(challenge1.replace("Everyone","All"))

#Split the string 'Coding For All' using space as the separator (split()) .
challenge = "Coding For All"
print(challenge.split())

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company.split(","))

#What is the character at index 0 in the string Coding For All.
challenge = "Coding For All"
print(challenge[0])

#What is the last index of the string Coding For All.
challenge = "Coding For All"
print(challenge[-1])

#What character is at index 10 in "Coding For All" string.
challenge = "Coding For All"
print(challenge[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
#acronym = first letters of words in a phrase and making a new word or short form.
#abbreviation = shortened form of a word or phrase. It doesn’t always use just the first letters.
challenge1 = "Python For Everyone"
acronym = "".join(word[0] for word in challenge1.split())
abbreviation = ".".join(word[0] for word in challenge1.split())
print(acronym)      #new word made from initials.
print(abbreviation) #shortened version of a word/phrase.

#Create an acronym or an abbreviation for the name 'Coding For All'.
challenge = "Coding For All"
acronym = "".join(word[0] for word in challenge.split())
abbreviation = ".".join(word[0] for word in challenge.split())
print(acronym) 
print(abbreviation) 


#Use index to determine the position of the first occurrence of C in Coding For All.
challenge = "Coding For All"
print(challenge.index("C"))

#Use index to determine the position of the first occurrence of F in Coding For All.
challenge = "Coding For All"
print(challenge.index("F"))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
challenge3 = "Coding For All People"
print(challenge3.rfind("l"))


#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index("because"))
print(sentence.find("because"))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex("because"))
print(sentence.rfind("because"))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
result = sentence.replace("because because because", "because")
print(result)
start = sentence.find("because because because")
end = start + len("because because because")
res = sentence[:start] + sentence[end:]
print(res)


#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find("because"))

#Does 'Coding For All' start with a substring Coding?
challenge = "Coding For All"
print(challenge.startswith("Coding"))

#Does 'Coding For All' end with a substring coding?
challenge = "Coding For All"
print(challenge.endswith("coding"))


#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
c1 = '   Coding For All      '  
print(c1.strip()) 
print(c1.lstrip()) 
print(c1.rstrip()) 


#Which one of the following variables return True when we use the method isidentifier():
w1 = "30DaysOfPython"
w2 = "thirty_days_of_python"
print(w1.isidentifier())
print(w2.isidentifier())


#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
space = " ".join(libraries)
hash = "#".join(libraries)
print(space)
print(hash)

#Use the new line escape sequence to separate the following sentences. I am enjoying this challenge.I just wonder what is next.
s1 = "I am enjoying this challenge.\nI just wonder what is next."
print(s1)

#Use a tab escape sequence to write the following lines. Name      Age     Country   City
print("Name\tAge\tBranch\tCity")
print("Srushti\t20\tCSE\t\tbanglore")
print(f"{'Name':<10}{'Age':<5}{'Branch':<10}{'City':<10}")      #for alignment
print(f"{'Srushti':<10}{'20':<5}{'CSE':<10}{'Bangalore':<10}")


#Use the string formatting method to display the following: area of circle
radius = int(input("Enter the radius : "))
area = 3.14 * radius**2
print("The area of a circle with radius {} is {} meters square.".format(radius,area))
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")


#Make the following using string formatting methods:
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")