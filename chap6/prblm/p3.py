#spam or not
s1 = "Make a lot of Money"
s2 = "buy now"
s3 = "subscribe this"
s4 = "click this"

msg = input("enter comment: ")

if ((s1 in msg) or (s2 in msg) or (s3 in msg) or (s4 in msg)):
    print("this is spam comment")
else:
    print("this is not spam comment")
