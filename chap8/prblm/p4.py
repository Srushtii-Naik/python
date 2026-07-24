#Sum of first n natural numbers (recursive)
def natural(n):
    if n==0:        #Base case: if n is 0, sum is 0      
        return 0
    else:
        return n + natural(n-1)      # Recursive case: n + sum of first (n-1) numb

print(natural(5))
# How it works: natural(5) = 5 + 4 + 3 + 2 + 1 + 0 = 15