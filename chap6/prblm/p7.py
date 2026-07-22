#post is abt user of not

post = ("Srushti is goog girl. Srushti is CSE student. she is now 3yr student. she is 20 now")
name = input("Enter name : ")

if name.lower() in post.lower():
    print(f'post is abt "{name}" ')
else:
    print(f'post is not  abt "{name}" ')