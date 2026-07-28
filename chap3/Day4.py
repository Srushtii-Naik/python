# #Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# s1 = 'Thirsty'
# s2 = 'Days'
# s3 = 'of'
# s4 = 'Python'
# res = s1 + s2+ s3+ s4
# print(res)
#  #or
# word = ['Thirty', 'Days', 'Of', 'Python']
# res = ' '.join(word)
# print(res)


# #Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# s1 = 'coding'
# s2 = 'for'
# s3 = 'all'
# print(f"{s1} {s2} {s3}")

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