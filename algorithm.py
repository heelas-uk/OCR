choice = 0
while not (choice>0 and choice<4):
    print("1. Play Game")
    print("2. Change character")
    print("3. Quit")
    try:
        choice = int(input())
    except ValueError:
        choice = 0
print("Bye!")
