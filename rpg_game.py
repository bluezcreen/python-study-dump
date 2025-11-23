import random
import time

#some stats
ehp = 50
php = 50
ehp = max(0, min(ehp, 50))
php = max(0, min(php, 50))

eatk = random.randint(8,25)
patk = random.randint(5,20)
pturn = True

#battle system
while ehp > 0 and php > 0:
	
	#player's turn'
	if pturn == True:
		move = input(f"""Fight (F) / PSI (P) / Run away (R) / Do nothing (D)
		Enemy HP {ehp}/50
		Player HP {php}/50""").strip().upper()
		time.sleep(1)
		
		#fight move
		if move == "F":
			print("Player attacks!")
			time.sleep(1)
			ehp = (ehp - patk)
			
			#crit text
			if patk >=18:
				time.sleep(1)
				print("SMAAAASH!!!")
			else:
				pass
				
			print(f"Enemy took {patk} damage!")
			print(f"""Enemy HP {ehp}/50
			Player HP {php}/50""")
			pturn = False
			
		#PSI move
		elif move ==  "P":
			chpsi = input("""
			(S)hield - 0PP
			(H)ealing - 0PP""")
			
			#heal
		#run move
		elif move == "R":
			print("Player tried to run away...")
			time.sleep(2)
			chance = random.randint(1,2)
			if chance == 1:
				print('...and did!')
				ehp = 0
			else:
				print("...but couldn't!")
				pturn = False
				
		#waste turn
		elif move == "D":
			print("Player is being absentminded.")
			pturn = False
			
		#invalid move
		else:
			print("That is not a valid move!")
			pturn = True
			
	#enemy turn
	else:
		time.sleep(2)
		print("Enemy attacks!")
		time.sleep(1)
		php = (php - eatk)
		
		#crit text
		if eatk >= 20:
			time.sleep(1)
			print("SMAAAASH!!")
		else:
			pass
			
		print(f"Player took {eatk} damage!")
		print(f"""Enemy HP {ehp}/50
		Player HP {php}/50""")
		pturn = True
		
#win/lose
if ehp <= 0:
		print("YOU WON!")
elif php <= 0:
		print("Player got hurt and collapsed...")
		print("Player lost the battle...")
else:
		pass
		