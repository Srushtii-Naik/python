#loops in python
'A loop is used to execute a block of code repeatedly until a condition becomes false or all items in a sequence are processed.'
# --------------------------------------------------------------------------------------------------------------------------------------

"FOR loops"          "iterate over a sequence"
#list for loop
lst =["Srushti","CSE",'E',20]
for i in lst:
    print(i)

#tuple 
t = (1,"SRUSHTI","DSATM",'E')
for i in t:
    print(i)

#string
name = "Srushti"
for ch in name:
    print(ch)

#dictionary
d = {"srushti":"girl", "age":20,"branch":"CSE"}
for key in d:
    print(key,":" ,d[key])

#sets
s = set()
for i in range(5):
    s.add(i)
    print(s)

#Range
for i in range(2,20,2):
    print(i)

# ------------------------------------------------------------------------------------------------------

"while loop"    "exectues as long as the condition is True."

count = 1
while(count<=5):
    print(count)    #1st print
    count+=1        #then increase


#infinate loop
while True:
    print("hi")
"to solve infinate loop v use loop control statements"

# ---------------------------------------------------------------------------------------------------------------------

"Loop Control Statements"

#break    "immediately terminates loop"
for i in range(1,10):
    if i==5:
        break 
    print(i)

#continue   "skip current iteration nd moves to nxt one"
for i in range(1,10):
    if i==5:
        continue
    print(i)

#pass      "does nthng, act as placeholder"
for i in range(5):
    pass
for i in range(1,3):
    print(i)

# --------------------------------------------------------------------------------------------------------

"Nested Loops --------loop inside another loop"

for i in range(2,5):
    for j in range(1,5):
        print(i,j)

#example---loops is for tables.
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end="\t")
    print()


# ------------------------------------------------------------------------
'''Python allows an else block with both for and while loops.
The else block executes only if the loop finishes normally (i.e., it is not terminated by break).'''

#eg
for i in range(5):
    print(i)
else:
    print("loop done!")


#eg with break
for i in range(5):
    if i==3:
        break   #does not execute because the loop ended with break.
    print(i)
else:
    print("done!")
