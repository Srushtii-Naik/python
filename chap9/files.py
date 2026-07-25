#File Handling (File I/O) in Python
'reading data from a file and writing data to a file'
'Instead of storing data only in memory (RAM), we store it permanently in files'


#Types of Files
"Text Files (.txt, .csv, .py) ----------Contains readable characters"
"Binary Files (.jpg, .png, .pdf, .exe) -------Contains data in binary format (0s,1s)"

# ______________________________________________________________________________________________________________________________________________________________________________________________________________

#Opening a File
# file = open("filename","mode") 
file = open("files.py")

'''
#File Modes
f = open("filename","r")    #read(default)
f = open("filename","w")    #write(create or overwrite)
f = open("filename","a")    #add data = end
f = open("filename","x")    #creates new 
f = open("filename","r+")   #read,write
f = open("filename","w+")   #read,write
f = open("filename","a+")   #read, append
f = open("filename","rb")   #read binary
f = open("filename","wb")   #write binary
f = open("filename","rt")   #read text
f = open("filename","wt")   #write text

'''
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________

'Reading a File'

# read()        Reads the entire file
file = open("file.txt","r") #if no r , by default is read
content = file.read()
print(content)
file.close()

#read(n)        Reads only n characters
file = open("file.txt","r")
content = file.read(10)
print(content)
file.close()

#readline()     Reads one line at a time
file = open("file.txt","r")
print(file.readline())
print(file.readline())
file.close()

#readlines()     Returns all lines as a list
file = open("file.txt","r")
print(file.readlines())
file.close()

# _________________________________________________________________________________________________________________________________________________________________________________

'Writing to a file'
'''Creates a new file if it doesn't exist
If it exists, all previous content is erased.'''

file =open("p1.txt","w")       #Existing content is deleted.
file.write("Python")
file.close()

#_____________________________________________________________________________________________________________________________________

'Appending to a File-----------------a mode adds data at the end.'
file = open("p1.txt","a")
file.write("\nProgramming")
file.close()

# _________________________________________________________________________________________________________________________________________

'Creating a New File'
file = open("new.txt","x")
file.close()
#If the file already exists: FileExistsError

#____________________________________________________________________________________________________________________________________________

'Closing a File---------Always close a file after using it'
file.close()

#__________________________________________________________________________________________________________________________________

'with Statement---------The file is closed automatically, even if an error occurs'
with open("p1.txt","r") as file:
    print(file.read())