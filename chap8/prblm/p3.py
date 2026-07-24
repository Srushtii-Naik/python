# Prevent print() from adding newline

print("Hello!",end=" ")     # Ends with space instead of newline
print("Srushti")

print("Hello!",end="")      # Ends with nothing
print("Srushti")

print("Hello!",end="---")   # Ends with custom string
print("Srushti")





print("A", end="")    # No newline
print("B")            # Output: AB

print("A", end="***") # Custom ending
print("B")            # Output: A***B