import random as r
bal = float(1.00)
chars = ["🍒", "🔔", "🍋", "🍊", "💀", "⭐"]
slot1 = r.randrange(0, 5)
slot2 = r.randrange(0, 5)
slot3 = r.randrange(0,5)

while bal>0:
    if input("Play y/n ") == "n":
        print("Balence is: " + str(bal))
        quit("99% of gamblers quit before they win big")
    else:
        1+1
    