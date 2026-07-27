#sum

nums = [1,4,7,2,5]
print("Sum: ",sum(nums))

# ___________________________________________________________________________________________________________________________________________________________________________________

lst = []
num = int(input("enter num of numbers: "))
for i in range(num):
    val =int(input(f"enter {i+1} num: "))
    lst.append(val)
total = sum(lst)
print(total)

# ___________________________________________________________________________________________________________________________________________________________________________________
num = int(input("enter num of numbers: "))
total = 0
for i in range(num):
    val =int(input(f"enter {i+1} num: "))
    total += val
print(total)

# ___________________________________________________________________________________________________________________________________________________________________________________
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum of numbers:", sum(nums))

# ___________________________________________________________________________________________________________________________________________________________________________________
from functools import reduce
nums = list(map(int, input("Enter numbers separated by space: ").split()))
total = reduce(lambda x, y: x + y, nums)
print("Sum of numbers:", total)
