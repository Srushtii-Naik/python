#string methods

a = "Srushti naik"
print(a)
print(a.upper())            #Upper letters
print(a.lower())            #lower letters
print(a.startswith("Sr"))    #check starts with Sr
print(a.endswith("ti"))     #check ends with ti
print(a.capitalize())         #capaitalize only 1st word not all even after space 
print(a.title())              #capaitalize each word  all even after space 
print(a.count("i"))         #counts occurences  
print(a.find("u"))          #Returns index of substring


b = " Srushti , Naik"
print(b)
print(b.strip())              #removes Spaces
print(b.replace("s","h"))       #Replaces text
print(b.split(","))         #Splits into a list

