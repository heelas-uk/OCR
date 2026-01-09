import secrets
num = int(input("Please enter the number of bytes you would like your password to be: "))
password = str(secrets.token_urlsafe(num))
with open("pass.sir_pilot_in_command", "w") as f:
    f.write(password)
