import random, os, time
print("===============")
print("character generator")
print("===============")
time.sleep(1)
os.system("clear")

def genHP():
	#roll a d8 and a d12
	d8 = random.randint(1,8)
	d12 = random.randint(1,12)
	#formula for hp
	hp = (((d8 * d12) / 2) + 10)
	return hp
	
def genOFF():
	#roll a d6 and a d8
	d6 = random.randint(1,6)
	d8 = random.randint(1,8)
	#formula for off.
	off = (((d6 * d8) / 2) + 12)
	return off

#HP
#((D8*D12) / 2) + 10
#offense
#((D6 * D8) / 2) + 12

makeanother = ("yes")
while makeanother == "yes":
	name = input("name this character: ")
	type = input("what do they wield? (weapon/power)")
	
	hp = genHP()
	off = genOFF()
	print(f"Character: {name}")
	print(f"Wields {type}")
	print(f"HP: {hp}")
	print(f"Offense: {off}")
	
	makeanother = input("Make another character? Yes/No").strip().lower()


	

