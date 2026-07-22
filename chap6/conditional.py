#Conditional Statements in Python
"allows pgrm to make decisions. based on T or F , exectues diff block of code"

#Types of Conditional Statements

#if Statement   "only if  condition is True."
age = 20
if age >= 18:
    print("Eligible to vote")

#if-else Statement "2 possb cond"
age = 20
if age >=18:
    print("Eligible to vote")
else:
    print("Not eligible")

#if-elif-else Statement   "multiple cond"
age = 0
if age >=18:
    print("Eligible to vote")
elif age < 18:
    print("Not eligible")
else:
    print("Invalid")

#Nested if   "if statement inside another if"
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")