# Stone Scissor Paper Game
import random
print("------------Let's Begin The Game------------")
weapons=["Stone","Paper","Scissor"]
a=0
b=0
i=0
name=input("Enter Your Name:- ")
while(i<10):
    print("Game - ",i+1)
    while(True):
        print("Weapons are 1-Stone 2-Paper 3-Scissor")
        player=input("Enter Your Weapon:- ")
        print(name+"'s Weapon - "+player)
        computer=random.choice(weapons)
        print("Computer's Weapon - "+computer)
        if(player=="Stone" and computer=="Scissor"):
            print(name+" Won")
            a=a+1
        elif(player=="Stone" and computer=="Paper"):
            print("Computer Won")
            b=b+1
        elif (player=="Scissor" and computer=="Paper"):
            print(name+" Won")
            a=a+1
        elif (player == "Scissor" and computer == "Stone"):
            print("Computer Won")
            b = b + 1
        elif (player == "Paper" and computer == "Stone"):
            print(name+" Won")
            a=a+1
        elif (player == "Paper" and computer == "Scissor"):
            print("Computer Won")
            b = b + 1
        elif player==computer:
            print("Game Draw")
        else:
            print("Enter Correct Weapon")
        break
    i=i+1
print(name+" Points = ",a)
print("Computer Points = ",b)
if(a>b):
    print("You Have Won The Game")
elif(b>a):
    print("Computer Has Won The Game")
else:
    print("Match Tied")





















