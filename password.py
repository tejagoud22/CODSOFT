from random import choice,shuffle
from string import ascii_letters,digits
s=ascii_letters+'@#%$^&*'+digits
def pas(x):
    for i in range(int(num)):
        shuffle(list(s))
        print(choice(s),end="")
    
while True:
    num=input("enter your number: ")
    if num.isdigit():
        pas(num)
        break
    else:
        print("ENTER POSITIVE NUMBER ONLY")
        




      