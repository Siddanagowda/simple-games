import random
def play(player , computer):

    if(player==computer):
        return "tie"
    elif (player == "snake" and computer == "water") or (player == "water" and computer == "gun") or (player == "gun" and computer == "snake"):
        return "player"
    else:
        return "computer"

count=0
a=int(input("enter the times to play : "))
n=1

for i in range (a):
    choices=["snake","water","gun"]
    print("enter snake=1,water=2,gun=3 : ")
    computer=random.choice(choices)

    player1=int(input())
    if(player1==1):
        player="snake"
    elif(player1==2):
        player=="water"
    elif(player1==3):
        player="gun"
    else:
        print("invalid key enter once more")
        continue
            

    result=play(player,computer)        
    if(result=="tie"):
        print("match is tied!")
    elif(result=="player"):
        print("WOW! You Won The Match")
        count+=1
    elif(result=="computer"):
        print("Sorry You lost the match")

    # i=i+1

    # print("enter y for continue and n for end ")
    # ch=input()
    # if(ch=="y"):
    #     n=1
    # else:
    #     break

print(f"your score is {count} out off {a} ")


