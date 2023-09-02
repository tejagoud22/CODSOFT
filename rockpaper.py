#project
#rock paper scissors....game...
import random
rock=1
paper=2
scissors=3
c=1
print("Welcome")
b=''
print("lets start the game")
print()
rounds=user_score=computer_score=Tie=0
while(True):
    if c==1:
        print("if you want to start the game enter s")
        print("if you want to Quit the game enter q")
        
        b=input("Enter your choice:")
        if b=='q':
            break
    if b=='s' or c==0:
        r=random.randint(1,3)
        print("choose rock or paper or scissors")
        rounds+=1
        a=input("Enter your choice:")
        if a=="rock":
            a=rock
        elif a=="paper":
            a=paper
        elif a=="scissors":
            a=scissors
        else:
            print("Wrong Input")
            c=0
        if r==a:
            print(40*"*")
            print("choose again, Its  a Tie ")
            Tie+=1
            print(40*"*")
            c=0
        if r==1 and a==2:
            print(40*"*")
            print("you won the game, the computer choosed rock")
            user_score+=1
            print(40*"*")
            c=1
        elif r==1 and a==3:
            print(40*"*")
            print("you loss the game, the computer choosed the rock")
            computer_score+=1
            print(40*"*")
            c=1
        elif r==2 and a==1:
            print(40*"*")
            print("you lost the game, the computer choosed the paper")
            computer_score+=1
            print(40*"*")
            c=1
        elif r==2 and a==3:
            print(40*"*")
            print("you won the game, the computer choosed the paper ")
            user_score+=1
            print(40*"*")
            c=1
        elif r==3 and a==1:
            print(40*"*")
            print("you won the game, the computer choosed the scissors")
            user_score+=1
            print(40*"*")
            c=1
        elif r==3 and a==2:
            print(40*"*")
            print("you lost the game, the computer choosed the scissors")
            computer_score+=1
            print(40*"*")
            c=1
    else:
        print("please choose the 'q' or 's' only")
print(60*"*")
print("Total rounds:",rounds,"|computer score:",computer_score,"|user score:",user_score,"|No of Tie's:",Tie)        
print(60*"*")      