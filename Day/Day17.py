# #'Exception Handling'
# 'An exception is an error that occurs while the program is running (runtime)'

# '#Types of Errors in Python'

# #Syntax Error : Occurs when Python syntax is incorrect.
# if True
#     print("Hello")  #o/p: SyntaxError

# #Runtime Error (Exception) : Occurs while the program is running.
# 10 / 0  #o/p: ZeroDivisionError

# #Logical Error: The program runs successfully but produces the wrong result.
# a = 10
# b = 5
# print(a - b)

# ___________________________________________________________________________________________________________________________________________________________________________________

# 'try and except'

# try:    #The try block contains code that might raise an exception
#     a = 10
#     b = 0
#     print(a/b)
# except: #The except block handles the exception
#     print("Cannot divide by zero")


#It is better to catch specific exceptions rather than using a generic except
# try:
#     num = int(input("Enter num: "))
# except ValueError:
#     print("please enter a valid integer")

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("division by 0 is not allowed")


#Multiple Exceptions
# try:
#     num = int(input("enter number: "))
#     print(10 / num)
# except ValueError:
#     print("invalid input")
# except ZeroDivisionError:
#     print("cnt divide by 0")

# try:
#     num = int(input("enter number: "))
# except ValueError:
#     print("invalid input")
# else:
#     print("you entred : ",num)



# #The finally block always executes, whether an exception occurs or not
# try:
#     print(10/2)
# except ZeroDivisionError:
#     print("error!")
# finally:
#     print("program finished")

# try:
#     num = int(input("Enter numb: "))
#     print(100 / num)
# except ValueError:
#     print("invalid number")
# except ZeroDivisionError:
#     print("Zero not allowed")
# else:
#     print("Calcuation Successful")
# finally:
#     print("Thank You!")

# ___________________________________________________________________________________________________________________________________________________________________________________

# #Raising Exceptions: You can raise your own exception using raise
# age = 15
# if age < 18:
#     raise ValueError("age must be atleast 18")

# #Custom Exceptions: You can create your own exception class.
# class InvalidAgeError(Exception):
#     pass
# age = 15
# if age < 18:
#     raise InvalidAgeError("Not Eligible")


# ___________________________________________________________________________________________________________________________________________________________________________________

#Common Built-in Exceptions
try:
    name = input("enter name: ")
    year_born = (input('year you were born: '))
    age = 2026 - year_born
    print(f'you are {name} and your age is {age}')
except TypeError:
    print('Wrong data type')
except NameError:
    print('Variable not defined')
except ValueError:
    print('value not correct')
except ZeroDivisionError:
    print('Divide by zero not allowed')
except IndexError:
    print('Invalid list index')
else:
        print('I usually run with the try block')
finally:
    print('I alway run.')


#It is also shorten the above code as follows:
try:
    name = input("Enter name")
    year_born = input('year u born: ')
    age = 2026 -year_born
    print(f'you are {name} and your age is {age}')
except Exception as e:
    print(e)



