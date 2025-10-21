import random as ran
print("Welcome to the number game")

total = 25

while total >0:
    p2 = total%4
    total -= p2 
    print("Ai took "+str(p2) + " tokens meaning there are "+ str(total))
    p1 = int(input("Player input a number to take away from "+ str(total)+ " : "))
    if p1 == 1:
        print("Player loses")
    else:
        if p1 > 3 or p1 < 0:
            p1 = ran.randrange(1,3,1)
            print("Invalid stupid automatically picking: " + str(p1))
            total -= p1
            if total <0:
                print("You lose becuase your stupid and went below 0")
            else:
                print("Current total is: " + str(total))
