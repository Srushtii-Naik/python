#String
'''Strings store text data.
They are immutable.
Support indexing and slicing.
Can be concatenated (+) and repeated (*).
Provide many useful built-in methods like upper(), lower(), split(), replace(), and join().
Use f-strings for clean and readable string formatting.'''


#Concatenation using "+"
a = "Srushti"
b = "Naik"
print("Concatenation: ", a + " " + b)


#String Repetition
print("Hello " *4)
print("Hello\n" *3)


#Checking Strings
a = "Srushti123"
print(a.isalpha())             #check it is alphabet??
print(a.isdigit())             #check it is digit??
print(a.isalnum())             #check it is both alpha nd num
print(a.startswith("Sru"))   #check it starts with Sru
print(a.endswith("123"))    #check it ends with 123


#String Formatting
name = "Srushti"
age = 20
print("1.f-strings (Recommended) Method")
print(f"Name is {name} and AGE is {age}")
print("2.format() Method")
print("Name is {}".format("Srushti"))
print("Age is {}".format(20))
print("3.% Formatting (Older Style)")
print("Name is %s." % "Srushti")
print("Name is %d." % 20)


# String Membership
# Use the in operator to check if a substring exists.
text = "Python Programming"
print("Python" in text)    # True
print("Java" in text)      # False


# Strings are Immutable
# You cannot modify a character directly.
text = "Python"
# This will cause an error:
# text[0] = "J"
# Correct way:
text = "J" + text[1:]
print(text)   # Jython