import s

poke = [ ["Name", "Element", "Ability", "HP", "MP"]]
def cprint():
	print()
	for row in poke:
			print("=================================================================================")
			for item in row:
				print(f"{item:^13}", end=" | ")
			print()
			
#stuff
pName = " "
pElement = " "
pAbility = " "
pHP = " "
pMP = " "

#element
elem = ["⚪Normal", "🔥Fire", "💧Water", "🪨Rock", "🔮Psychic", "💨Air", "⚡Electricity"]

while True:
		#pAbility and pElement
	pElement = s.r_choice(elem)
	if "Fire" in pElement:
		pAbility = "Dragon breath"
	elif "Water" in pElement:
		pAbility = "Tsunami"
	elif "Rock" in pElement:
		pAbility = "Earthquake"
	elif "Psychic" in pElement:
		pAbility = "Hypnotize"
	elif "Air" in pElement:
		pAbility = "Tornado"
	elif "Electricity" in pElement:
		pAbility = "1000V shock"
	else:
		pAbility = "Melee attacks"
	
	print("You found a mysterious animal!")
	
	pName = input("Give it a name: ")
	s.delay(0.5)
	
	print(f"Looking at the animal, it seems to be posessing {pElement} power!")
	s.delay(0.5)
	
	print(f"It can do a {pAbility}!")
	s.delay(0.5)
	
	pHP = s.r_int(100,450)
	pMP = s.r_int(50, 85)
	print(f"It has {pHP} HP and {pMP} MP!")
	s.delay(0.5)
	
	print("You logged this to your journal...")
	poke.append([pName, pElement, pAbility, pHP, pMP])
	s.delaclear(1)
	cprint()
	print()
	s.delaclear(0, True, "press enter to continue")