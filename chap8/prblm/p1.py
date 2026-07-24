#greatest of 3 num
def greatest(a,b,c):
    if a>b and a>c:      # Compare a with b and c
        return a         # a is greatest
    elif b>a and b>c:
        return b         # b is greatest
    elif c>a and c>b:
        return c         # c is greatest
    else:
        return None

print(greatest(10,45,23))




#max fun
def greates(a,b,c):
    return max(a,b,c)
print(greatest(10,25,67))