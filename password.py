password = "secret"
attempt = 0
while attempt <3:
    guess = input("Please enter your password: ")
    if guess == password:
        print("You are correct welcome")
        break
    else:
        print("Incorrect try again")
        attempt += 1

if attempt == 3:
    print("You failed")
    exit(1)
else:
    exit(0)
