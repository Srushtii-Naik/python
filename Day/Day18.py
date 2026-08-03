# 'Regular Expressions (RegEx) in Python'
# #special text string that helps to find patterns in data
# #we should import the RegEx module which is called re

# #verify if the email format
# import re
# email = "abc@gmail.com"
# pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-z]{2,}$"
# if re.match(pattern,email):
#     print("valid email")
# else:
#     print("Invalid Email")

# ___________________________________________________________________________________________________________________________________________________________________________________


'Methods in re Module'


# #re.match() : Checks whether the pattern matches from the beginning of the string
# import re
# text = "python is easy"
# result = re.match("python",text)
# print(result)
# print(result.group())   #To display the matched text
# span = result.span()
# print(span)         # We can get the starting and ending position of the match as tuple using span
# start, end = span   #start and stop position from the span
# print(start,end)
# substring = text[start:end]
# print(substring)

# import re
# text = 'I love Python'
# result = re.match("python",text)
# print(result)       #None: Because match() only checks the beginning of the string.


# #re.search(): Searches the entire string.
# import re
# text = "i love python"
# result = re.search("python",text)
# print(result)
# print(result.group())   #looks through the whole string


# #re.findall() : Returns all occurrences of the pattern
# text = 'cat, rat, bat, cat'
# result = re.findall('cat',text)
# print(result)
# num = '1 2 3 4 5'
# print(re.findall(r'\d',num))


# #re.finditer() : Returns match objects one by one
# import re
# text = 'cat, rat, bat, cat'
# matches = re.finditer("cat",text)
# for match in matches:
#     print(match.start(),match.group())

# #re.sub() : Replaces matched text
# import re
# text = 'i love java'
# new = re.sub("java","python",text)
# print(new)

# #re.split(): Splits a string using a regex pattern
# import re
# name = "Srushti, Ashok, Naik"
# text = re.split(",",name)
# print(text)

# txt = '''I am teacher and  I love teaching.
# There is nothing as rewarding as educating and empowering people.
# I found teaching more interesting than any other jobs.
# Does this motivate you to be a teacher?'''
# print(re.split('\n',txt))

# import re
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''
# matches = re.findall('python',txt,re.I)   #re.I both lowercase and uppercase letters are included
# print(matches)
# matches = re.findall('python|Python',txt)   
# print(matches)
# matches = re.findall('[Pp]ython',txt,re.I)   
# print(matches)


# #Replacing a Substring
# import re
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''
# match = re.sub('Python|python', 'JavaScript',txt)
# print(match)
# match = re.sub('[Pp]ython','javaScript',txt)
# print(match)

# txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
# T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
# I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
# D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
# matches = re.sub("%",'',txt)
# print(matches)

# # ___________________________________________________________________________________________________________________________________________________________________________________


# #Writing RegEx Patterns
# 'To declare a string variable we use a single or double quote. To declare RegEx variable (r'') '
# import re
# pattern = r'apple'
# txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
# matches = re.findall(pattern, txt)
# print(matches)
# matches = re.findall(pattern,txt,re.I)
# print(matches)
# pattern = r'[Aa]pple'
# matches = re.findall(pattern, txt)
# print(matches)

# # ___________________________________________________________________________________________________________________________________________________________________________________


# 'Regex Special Characters'

# import re
# text = 'i love python'
# print(re.findall("c.t","cat cut cot cup cum"))      # .(dot): Matches any single character
# print(re.search('^i',text))                 # ^ : Matches the start of the string.
# print(re.search("python$",text))            # $ : Matches the end of the string.
# print(re.findall('ab*', "a ab abb abbb "))  # * :Matches zero or more occurrences.
# print(re.findall('ab+', 'a ab abb abbb'))   # + :Matches one or more occurrences.
# print(re.findall('ab?', "a ab abb abbb "))  # ? :Matches zero or one occurrences.
# print(re.findall(r'\d',"abc123"))           # \d : Matches any digit.
# print(re.findall(r'\D',"abc123"))           # \D : Matches non-digit characters.
# print(re.findall(r'\w',"abc_123"))          # \w :Matches letters, digits, and underscore.
# print(re.findall(r'\W',"abc@123"))          # \W :Matches non-word characters.
# print(re.findall(r'\s','hello world!'))     # \s :Matches whitespace
# print(re.findall(r'\S','hello world!'))     # \S :Matches non-whitespace
# pattern = 'i love python 1234567890'
# print(re.findall(r'[^a-zA-Z]',pattern))     # ^(Negation)  : ^ in set character means negation, not A to Z, not a to z, no space


# # ___________________________________________________________________________________________________________________________________________________________________________________


# #What is the most frequent word in the following paragraph?
# import re
# paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love'
# words = re.findall(r'\b\w+\b',paragraph)
# #\b → Word boundary (start/end of a word)
# #\w+ → One or more letters, digits, or _
# #\b\w+\b → Matches a complete word , while ignoring punctuation such as ., ,, !, ?
# freq = {}
# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1
# res = sorted(freq.items(),key = lambda x: x[1], reverse = True )
# output = [(count, word) for word, count in res]
# print(output)


# #The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles
# import re
# text = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1
# in the negative direction, 0 at origin, 4 and 8 in the positive direction."""
# # Extract numbers
# points = re.findall(r'-?\d+', text)
# print("Points:", points)
# #-? → Matches an optional minus (-) sign
# #\d+ → Matches one or more digits
# #-?\d+ → Matches both positive and negative integers


# # Convert to integers and sort
# sorted_points = sorted([int(i) for i in points])
# print("Sorted Points:", sorted_points)

# # Find the distance
# distance = sorted_points[-1] - sorted_points[0]
# print("Distance:", distance)

# 'or'


# import re
# text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction'
# points = re.findall(r'-?\d+', text)
# sorted_points = sorted(map(int, points))
# distance = sorted_points[-1] - sorted_points[0]
# print(points)
# print(sorted_points)
# print(distance)

# ___________________________________________________________________________________________________________________________________________________________________________________


# #Write a pattern which identifies if a string is a valid python variable
# import re
# def is_valid_variable(var):
#     return re.match(r'^[A-Za-z_]\w*$', var) is not None
# print(is_valid_variable('first_name'))   # True
# print(is_valid_variable('first-name'))   # False
# print(is_valid_variable('1first_name'))  # False
# print(is_valid_variable('firstname'))    # True


#Clean the following text. After cleaning, count three most frequent words in the string
import re
from collections import Counter
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. 
;I found tea@ching m%o@re interesting tha@n any other %jo@bs. 
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    return re.sub(r'[^A-Za-z\s]','',text)
cleaned_text = clean_text(sentence)
print(cleaned_text)
words = cleaned_text.split()
most_common = Counter(words).most_common(3)
print(most_common)