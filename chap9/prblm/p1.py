#Find 'twinkle' in poem
with open("f1.txt","r") as f:
    content = f.read()

if "twinkle" in content:
    print("twinkle is present in the file")
else:
    print("twinkle is not present in the file")
