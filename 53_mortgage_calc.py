print("Fake mortgage claculator for OCR coding challenges")

ten_year_rate = float(5.57)
fifteen_year_rate = float(5.6)
thirty_year_rate = float(6.31)

value = float(input("Please enter the value of your mortgage (with no currency signs) "))
mory = input("Would you like input the time in years or months (M or Y) ")
if mory == "M":
    months = float(input("Enter the number of months you want to pay off the mortgage over: "))
else:
    year = float(input("Enter the number of year you wnat the mortgage to run over: "))
    months = year*12

month_rate = float(input("Enter the APR of your loan (no percent signs) "))*12


monthly_fee = (value*month_rate*(1+month_rate)**months)/((1+month_rate)**months-1)
print("Your monthly payment is "+ str(monthly_fee) + " paid for "+ str(months/12) + " years")
