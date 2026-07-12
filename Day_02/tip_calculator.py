print("Welcome to the tip calculator!")
bill_amt = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10 12 15 "))
tip_amt=(tip_percent/100)*bill_amt
total_amt=bill_amt+tip_amt
count_people = int(input("How many people to split the bill? "))
eachperson_amt=total_amt/count_people
# print("$"+str(round(eachperson_amt,2)))
eachperson_amt_2decimal=round(eachperson_amt,2)
print(f"Each person should pay: ${eachperson_amt_2decimal}")



