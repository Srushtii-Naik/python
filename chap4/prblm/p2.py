#marks in sub nd sort

marks = []
f1 = int(input("Enter marks in sub 1: "))
marks.append(f1)
f2 = int(input("Enter marks in sub 2: "))
marks.append(f2)
f3 = int(input("Enter marks in sub 3: "))
marks.append(f3)
f4 = int(input("Enter marks in sub 4: "))
marks.append(f4)
f5 = int(input("Enter marks in sub 5: "))
marks.append(f5)
f6 = int(input("Enter marks in sub 6: "))
marks.append(f6)
f7 = int(input("Enter marks in sub 7: "))
marks.append(f7)

print(marks)

#sorting opt 1:
marks.sort()
print("marks in sorted: ",marks)

#sorting opt 2:
print("sorted: ",sorted(marks))