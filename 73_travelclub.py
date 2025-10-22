print("Welcome to the travel club expenses tracker")
print("To stop the tracker and get results enter STOP")
exp = ""
while exp != "STOP":
    exp = input("Enter the description of the expense ")    
    value = str(input("Enter the value of the transaction in pounds (no sign needed): "))
    with open("expenses_type.txt", "a") as a:
        a.write(exp + "  £" + value)
        a.close

    with open("total.txt", "w") as b:
        total = b.read()
        total += float(value)
        b.write(total)
        b.close
with open("expenses_type.txt", "r") as a:
    print(a.read())
    a.close
with open("total.txt", "r") as b:
    print("The total is: " + b.read())
    final = b.read()
    b.close

div = float(input("How many people to split between? : "))
print("Per person total is: "+ final/div)