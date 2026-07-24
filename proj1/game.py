import random               # For computer to make random choices

computer = random.choice([-1,0,1])
youstr = input("Enter ur choice(s,w,g): ")
youDict = {"s":1, "w": -1, "g":0}
reverseDict = {1:"Snake",-1:"water", 0:"Gun"}
you = youDict[youstr]

print(f"you chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("🤝 It's a draw!")
else:
    if computer == -1 and you == 1:
        print("You win! 🎉")
    elif computer == -1 and you == 0:
        print("You lose! 😢")
    elif computer == 1 and you == -1:
        print("You lose! 😢")
    elif computer == 1 and you == 0:
        print("You Win! 🎉")
    elif computer == 0 and you == -1:
        print("You Win! 🎉") 
    elif computer == 0 and you == 1:
        print("You Lose! 😢")
    else:
        print("Something went wrong!")

