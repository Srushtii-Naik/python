#Multiplication table
def table(n):
    for i in range (1,11):               # Loop from 1 to 10
        print(f"{n} X {i} = {n*i}")      # Print n × i = result
table(5)

# -------------------------------------------------------------------------------------------------------
#Multiplication table reverse
def table(n):
    for i in range(10,0,-1):         # Loop from 10 down to 1
        print(f"{n} X {i} = {n*i}")  # Print n × i = result
table(5)