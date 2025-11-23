from colorama import Fore, Back, Style
import random, time, s

poke = {
"Name" : None,
"Element" : None,
"Ability" : None,
"HP" : None,
"PP" : None
}

#element
elem = ["Normal", "Fire", "Water", "Rock", "Psychic", "Air", "Electricity"]
e = random.choice(elem)

#ability
if e == "Fire":
	color = Fore.RED
	poke["Ability"] = "Dragon breath"
elif e == "Water":
	color = Fore.BLUE
	poke["Ability"] = "Tsunami"
elif e == "Rock":
	color = Fore.BLACK + Back.WHITE
	poke["Ability"] = "Earthquake"
elif e == "Psychic":
	color = Fore.MAGENTA
	poke["Ability"] = "Hypnotize"
elif e == "Air":
	color = Fore.CYAN
	poke["Ability"] = "Tornado"
elif e == "Electricity":
	color = Fore.YELLOW
	poke["Ability"] = "1000V shock"
else:
	color = Fore.WHITE
	poke["Ability"] = "Melee attacks"

print("You found a mysterious animal!")

poke["Name"] = input("Give it a name: ")
time.sleep(0.5)

poke["Element"] = e

print(f"Looking at the animal, it seems to be posessing {e} power!")
time.sleep(0.5)

print(f"It can do a {poke['Ability']}!")
time.sleep(0.5)

poke["HP"] = random.randint(100,450)
poke["PP"] = random.randint(50, 85)
print(f"It has {poke['HP']} HP and {poke['PP']} PP!")
time.sleep(0.5)

print("You logged this to your journal...")
s.delaclear(1)

#color time
#color = " "

#if e == "Fire":
#	color = Fore.RED
#elif e == "Water":
#	color = Fore.BLUE
#elif e == "Rock":
#	color = Fore.BLACK + Back.WHITE
#elif e == "Psychic":
#	color = Fore.MAGENTA
#elif e == "Air":
#	color = Fore.CYAN
#elif e == "Electricity":
#	color = Fore.YELLOW
#else:
#	color = Fore.WHITE
	
for name, data in poke.items():
	print(f"{color}{name} : {data}")