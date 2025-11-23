import random
import time

#some stats
ehp = 50
php = 50
ppp = 20
ehp = max(0, min(ehp, 50))
php = max(0, min(php, 50))
ppp = max(0, min(ppp, 20))
patk = 0
#shield status
psp = 0
psp = max(0, min(psp, 100))

#debuffs
dbsleep = False

pturn = True

#start/reset program
while exit != True:
	
	#battle system
	print("Enemy approaches!")
	while ehp > 0 and php > 0:
		
		#player's turn'
		if pturn == True:
			move = input(f"""Fight (F) / PSI (P) / Run away (R) / Do nothing (D)
			HP {php}/50
			PP {ppp}/20
			SP {psp}/100""").strip().upper()
				
			time.sleep(1)
			#movecheck
			#fight move
			if move == "F":
				print("Player attacks!")
				time.sleep(1)
				patk = random.randint(5,20)
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
				cpk = input("""
				(I)nstakill (for debug purposes) - 20PP
				(Z)uicide (for debug purposes) -20PP
				(S)hield - 10PP
				(L)ifeup - 5PP
				(H)ypnosis - 10pp""").strip().upper()
				
				#lifeup
				if cpk == "L":
					if ppp >= 5:
						print("Player tried PK Lifeup!")
						time.sleep(1)
						heal = random.randint(10,20)
						php = min(50, heal + php)
						print(f"Player healed {heal} HP! HP is now {php}!")
						ppp = (ppp - 5)
						pturn = False
					else:
						print("Not enough PP!")
						pturn = True
														
				#shield
				elif cpk == "S":
					if ppp >= 10:						
						print("Player tried PK Shield!")
						time.sleep(1)
						psp += 50
						print(f"Player gained 50SP! SP is now {psp}!")
						ppp = (ppp - 10)
						pturn = False
					else:
						print("Not enough PP!")
						pturn = True
				
				#hypnosis
				elif cpk == "H":
					if ppp >= 10:
						dbsleep = True
						print("Player tried Hypnosis!")
						time.sleep(1)
						print("Enemy fell asleep!")
						ppp = (ppp - 10)
						pturn = False
					else:
						print("Not enough PP!")
						pturn = True
						
				#instakill
				elif cpk == "I":
					print("Player tried PK Instakill!")
					print("It worked fantastically!")
					ppp = (ppp - 20)
					ehp = 0
				
				#suicide
				elif cpk == "Z":
					print("Player tried PK Suicide!")
					print("Player felt an awful surge of depression...")
					php = 0
						
				#counter
				#if cpk == "C":
				
				#falsecheck
				else:
					print("Not a valid item")
					pturn = True
				
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
		
		#debuff check
			if dbsleep == True:
				print("Enemy is asleep...")
				pturn = True
				
				if patk > 10:
					print("Enemy woke up!")
					dbsleep = False
					pturn = True
					
				else:
					pass

			else:
				pass
			
		#enemy attack
		elif pturn == False:
			eatk = random.randint(10,25)
			time.sleep(2)
			print("Enemy attacks!")
			time.sleep(1)
			
			#crit text
			if eatk >= 20:
				time.sleep(1)
				print("SMAAAASH!!")
			else:
				pass
				
			#damage model and shieldcheck
			if psp > 0:
				seatk = int(eatk / 2)
				php = (php - seatk)
				print("Player's shield halved the attack!")
				print(f"Player took {seatk} damage!")
				#shield wear
				psp = (psp - seatk)
				pturn = True
			else:
				php = (php - eatk)
				print(f"Player took {eatk} damage!")
				print(f"""Enemy HP {ehp}/50
				Player HP {php}/50""")
				pturn = True
		
		else:
			pass
			
	#win/lose
	#win
	if ehp <= 0:
			print("Enemy became tame...")
			time.sleep(1)
			print("YOU WON!")
			rpl = input("Play again? Y/N").strip().upper()
			
			if rpl == "Y":
				exit = False
				ehp = 50
				php = 50
				psp = 0
				ppp = 20
				
			else:
				print("This program will end.")
				exit = True

	#lose			
	elif php <= 0:
			print("Player got hurt and collapsed...")
			print("Player lost the battle...")
			print("............")
			time.sleep(2)
			rst = input("""Player! It seems like you got your head handed down to you! Restart? Y/N""").strip().upper()
			if rst == "Y":
				print("Player gathered all of his courage and stood up again...")
				ehp = 50
				php = 50
				psp = 0
				time.sleep(2)
				
				exit = False
			elif rst == "N":
				print("This program will end.")
				exit = True
			else:
				pass
			