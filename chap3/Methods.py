# # #string methods

# # a = "Srushti naik"
# # print(a)
# # print(a.upper())            #Upper letters
# # print(a.lower())            #lower letters
# # print(a.startswith("Sr"))    #check starts with Sr
# # print(a.endswith("ti"))     #check ends with ti
# # print(a.capitalize())         #capaitalize only 1st word not all even after space 
# # print(a.title())              #capaitalize each word  all even after space 
# # print(a.count("i"))         #counts occurences  
# # print(a.find("u"))          #Returns index of substring


# # b = " Srushti , Naik"
# # print(b)
# # print(b.strip())              #removes Spaces
# # print(b.replace("s","h"))       #Replaces text
# # print(b.split(","))         #Splits into a list




# # ___________________________________________________________________________________________________________________________________________________________________________________

# #capitalize(): Converts the first character of the string to capital letter
# challenge = 'my name is Srushti'
# print(challenge.capitalize())

# #count(): returns occurrences of substring in string
# challenge = 'my name is Srushti im learning python'
# print(challenge.count('i'))
# print(challenge.count('i',7,18))
# print(challenge.count('is',7,18))

# #endswith(): Checks if a string ends with a specified ending
# challenge = 'my name is Srushti im learning python'
# print(challenge.endswith('on'))     

# #expandtabs(): Replaces tab character with spaces
# challenge = 'my name is Srushti\t im learning python'
# print(challenge.expandtabs())
# print(challenge.expandtabs(10))

# #find(): Returns the index of the first occurrence of a substring, if not found returns -1
# challenge = 'my name is Srushti im learning python'
# print(challenge.find('i'))
# print(challenge.find('is')) #1st index

# #rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
# challenge = 'my name is Srushti im learning python'
# print(challenge.rfind('i'))
# print(challenge.rfind('is'))

# #format(): formats string into a nicer output
# first_name = 'Srushti'
# last_name = 'Naik'
# age = 20
# branch = 'CSE'
# sentence = 'I am {} {}. I am {} year old. I am {} student.'.format(first_name,last_name,age,branch)
# print(sentence)

# #index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
# challenge = 'my name is Srushti im learning python'
# sub_string = 'Sru'
# print(challenge.index(sub_string))
# print(challenge.index(sub_string,9)) #sub_string = 'San'---->valueError

# #rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
# challenge = 'my name is Srushti im learning python'
# sub_string = 'Sru'
# print(challenge.rindex(sub_string))
# print(challenge.rindex(sub_string,9)) #sub_string = 'San'---->valueError


# #isalnum(): Checks alphanumeric character
# challenge = 'my name is Srushti im learning python'
# print(challenge.isalnum())  #False, space is not an alphanumeric character
# challenge1 = 'Srushti2006'
# print(challenge1.isalnum()) #True

'''
    isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
    isdecimal(): Checks if all characters in a string are decimal (0-9)     
    isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
    isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
    isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name

'''

# #islower(): Checks if all alphabet characters in the string are lowercase
# challenge = 'my name is Srushti im learning python'
# print(challenge.islower())      #False (Srushti "S")
# print(challenge.isupper())      #False


# #join(): Returns a concatenated string
# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# res = ' '.join(web_tech)
# print(res)

#strip(): Removes all given characters starting from the beginning and end of the string
challenge2 = "sspythoniss"
print(challenge2.strip("s"))    #Removes all s from start and end only.
print(challenge2.lstrip("s"))   #Removes s only from the left side (start).
print(challenge2.rstrip("s"))   #Removes s only from the right side (end).
print(challenge2.replace("s","*"))  #Removes all s inside the string, not just edges.

#split(): Splits the string, using given string or space as a separator
challenge = 'my name is Srushti im learning python'
print(challenge.split())

#title(): Returns a title cased string
challenge = 'my name is Srushti im learning python'
print(challenge.title())

#swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'my name is Srushti im learning python'
print(challenge.swapcase())

#startswith(): Checks if String Starts with the Specified String
challenge = 'my name is Srushti im learning python'
print(challenge.startswith("my"))