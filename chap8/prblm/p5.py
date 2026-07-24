#Pattern printing (n=3: ***, **, *)
 
def pattern(n):
    for i in range(n,0,-1):     # Loop from n down to 1
        print("*" * i)          # Print i stars in each row
print(pattern(3))
# n=3: i=3 → ***, i=2 → **, i=1 → *