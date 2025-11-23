print("loan calculator")

loan = int(input("ok how much money will u loan"))
time = int(input("ok now how long are you gonna pay for this"))
print("ight so we'll charge a 5% interest on you and...")
interest = (5 / 100)
addinterest = (interest * loan)

for i in range(time):
	print("Year", i + 1)
	#interest
	loan = loan + (interest * loan)
	print(round(loan, 2))