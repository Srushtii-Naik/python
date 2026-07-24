#Remove word from list and strip it
# strip() removes leading/trailing spaces (like spaces, tabs, or newline characters) from a string


def remove_strip(lst,word):
    new = []            # Create new list to store modified items

    for item in lst:         # Loop through each item in the list
        if item != word:     # Remove the word and strip extra spaces
            new.append(item.strip())
    return new
lst = [" Srushti"," Sanjana "," Sandesh "]
print(remove_strip(lst,"San"))

# ----------------------------------------------------------------------------

#using list comprehension
def remove_strip(lst,word):
    return [item.strip() for item in lst if item != word]
lst = [" Srushti"," Sanjana "," Sandesh "]
print(remove_strip(lst,"San"))





# strip() removes whitespace from both ends
"  Hello  ".strip()  # "Hello"
"  Srushti  ".strip()  # "Srushti"