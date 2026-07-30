#Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)

i=0
while i <= 10:
    print(i)
    i = i+1


#Iterate 10 to 0 using for loop, do the same using while loop
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i = i-1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle
for i in range(1,8):
    print(i * "#")


#Use nested loops to create the following
for i in range(1,8):
    for j in range(1,8):
        print("*",end=' ')
    print()

#Print the following pattern: Tables
for i in range(11):
    print(f"{i} X {i} = {i*i}")


#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for item in lst:
    print(item)

#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i%2 == 0:
        print(i)

#Use for loop to iterate from 0 to 100 and print only odd numbers\
for i in range(101):
    if i%2 != 0:
        print(i)


#Use for loop to iterate from 0 to 100 and print the sum of all numbers
total = 0
for i in range(101):
    total += i
print(total)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even =0
odd = 0
for i in range(101):
    if i%2==0:
        even += i
    else:
        odd += i
print("The sum of all evens is", even)
print("The sum of all odds is", odd)


# ___________________________________________________________________________________________________________________________________________________________________________________


#Loop through the countries and extract all the countries containing the word land.

countries = [
  'Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda',
  'Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain',
  'Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia',
  'Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso',
  'Burundi','Cabo Verde','Cambodia','Cameroon','Canada','Central African Republic',
  'Chad','Chile','China','Colombia','Comoros','Congo, Democratic Republic of the',
  'Congo, Republic of the','Costa Rica',"Côte d'Ivoire",'Croatia','Cuba','Cyprus',
  'Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','East Timor (Timor-Leste)',
  'Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Eswatini',
  'Ethiopia','Fiji','Finland','France','Gabon','Gambia','Georgia','Germany','Ghana',
  'Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras',
  'Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy',
  'Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South',
  'Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein',
  'Lithuania','Luxembourg','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta',
  'Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco',
  'Mongolia','Montenegro','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal',
  'Netherlands','New Zealand','Nicaragua','Niger','Nigeria','North Macedonia','Norway',
  'Oman','Pakistan','Palau','Palestine','Panama','Papua New Guinea','Paraguay','Peru',
  'Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis',
  'Saint Lucia','Saint Vincent and the Grenadines','Samoa','San Marino','Sao Tome and Principe',
  'Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia',
  'Slovenia','Solomon Islands','Somalia','South Africa','South Sudan','Spain','Sri Lanka',
  'Sudan','Suriname','Sweden','Switzerland','Syria','Tajikistan','Tanzania','Thailand',
  'Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda',
  'Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan',
  'Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe'
]

land = [country for country in countries if "land" in country]
print(land)


#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
rev = []
for i in range(len(fruits)-1, -1, -1):
    rev.append(fruits[i])
print(rev)
