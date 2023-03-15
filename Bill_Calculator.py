#Bill Calculator
#Parnia

welcomeText = print("Welcome to the Bill Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))


billForEach = (bill / people) * (tip / 100 + 1)
totalBillFormat = "{:.2f}".format(billForEach)

print(f"Each person should pay: ${totalBillFormat}")