import random

def rollInfDice(x):
	j = random.randint(1, x)
	print("bro rolled a", j)
	
program = ("yes")
print("infinite dice")


while program == "yes":
	n = int(input("number of sides: "))
	rollInfDice(n)
	exit = input("roll again? yes/no").strip().lower()