import random

#stats
ehp = 50
php = 50
atk = random.randint(1, 20)
eatk = random.randint(8,25)
pturn = "true"

#turn 1
print("Enemy approaches!")
print(f"Enemy {ehp}/50")

while pturn != "false":
	choice = input("Fight (F) | Heal (H) | Run away (R)").strip().upper()

##fight
	if choice == "F":
		print("Player attacks!")
	
	ehp = (ehp - atk)
	#crit
	if atk >= 18:
	    	print("SMAAAASH!!!")
	    	
	print(f"Enemy took {atk} damage!")
	print(f"Enemy {ehp}/50")
	print(f"Player {php}/50")
	pturn == "false"

#enemy turn
while pturn != "true":
	print("Enemy attacks!")
	php = (php - eatk)
	print(f"Player took {eatk} damage!")
	print(f"Enemy {ehp}/50")
	print(f"Player {php}/50")

#playerturn again