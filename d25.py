import random
print("bungeons and bragons type thing")

def D8andD6():
	x = random.randint(1,8)
	y = random.randint(1,6)
	z = (x*y)
	return z
	
makeanother = ("yes")
while makeanother == "yes":
	name = input("name this character: ")
	
	hp = D8andD6()
	print(f"Character: {name}")
	print(f"HP: {hp}")
	
	makeanother = input("Make another character? Yes/No").strip().lower()


	

