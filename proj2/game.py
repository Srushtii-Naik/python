#ROCK, PAPER, SCISSORS

import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice:(r,p,s) ")
youDict = {"r":0, "p":-1, "s":1}
reverseDict = {0:"Rock", -1:"Paper", 1:"Scissor"}
you = youDict[youstr]

print(f"you choose {reverseDict[you]} ")
print(f"computer choose {reverseDict[computer]} ")

if computer == you:
    print("🤝 It's a draw!")
else:
    if you == 0 and computer == 1:
        print("🎉 You Win! Congratulations!")
    elif you == 0 and computer == -1:
        print("You lose! 😢")
    elif you == 1 and computer == 0:
        print("You lose! 😢")
    elif you == 1 and computer == -1:
        print("You win! 🎉")
    elif you == -1 and computer == 0:
        print("You win! 🎉")
    elif you == -1 and computer == 1:
        print("You lose! 😢")
    else:
        print("Something went wrong!")

