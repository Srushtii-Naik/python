# #Write a function which generates a six digit/character random_user_id
# import random
# import string 
# def random_user_id():
#     char = string.ascii_letters + string.digits
#     id = ''.join(random.choice(char) for _ in range(6))
#     return id
# print(random_user_id())


# #Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# import random
# import string
# def user_id_gen_by_user():
#     length, count = map(int, input("Enter length and count: ").split())
#     char = string.ascii_letters + string.digits
#     ids = [''.join(random.choice(char) for _ in range(length) )for _ in range(count)]
#     return '\n'.join(ids)
# print(user_id_gen_by_user())

# #Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)
# import random
# def rgb_color():
#     r = random.randint(0,255 )
#     g = random.randint(0,255 )
#     b = random.randint(0,255 )
#     return f"rdb({r},{g},{b})"
# print(rgb_color())

# ___________________________________________________________________________________________________________________________________________________________________________________



#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random
def list_of_hexa_colors(n):
    colors = []
    for _ in range(n):
        color = "#" + ''.join(random.choice("0123456789adcdef") for _ in range(6))
        colors.append(color)
    return colors
print(list_of_hexa_colors(3))


#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
