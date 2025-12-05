import secrets
num = int(input("Please enter the number of bytes you would like your password to be: "))
password = str(secrets.token_urlsafe(num))
print(password)
with open("rand_pass.secure", "w") as f:
    f.write("Your password is: \n" + password)