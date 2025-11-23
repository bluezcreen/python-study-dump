import random, os, time

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

def clear():
	os.system("clear")
	
def wait():
	time.sleep(1)
	
print("===============")
print("worst rpg on earth")
print("a replit assignment ")
print("===============")
time.sleep(1)
os.system("clear")

#HP
#((D8*D12) / 2) + 10
#offense
#((D6 * D8) / 2) + 12
#damage model
#(offense1 - offense2) + 1
		
			#character 1
name1 = input("name this character: ")
type1 = input("what do they wield? (weapon/power)")
			
hp1 = genHP()
off1 = genOFF()
print(f"Character: {name1}")
print(f"Wields {type1}")
print(f"HP: {hp1}")
print(f"Offense: {off1}")
input()
clear()
			
			#character 2
name2 = input("name the character that will battle the one you just made")
type2 = input("what do they wield?")
			
hp2 = genHP()
off2 = genOFF()
print(f"Character: {name2}")
print(f"Wields {type2}")
print(f"HP: {hp2}")
print(f"Offense: {off2}")
p2 = (name2, hp2)
input()
clear()
		
atk = abs(off1 - off2 + 1)
#p1's attack'
def atk2():
	global hp2, atk
	hp2 -= atk

#p2's attack'
def atk1():
	global hp1, atk
	hp1 -= atk

#counters
turns1 = 0
turns2 = 0

print("battle start")
while hp1 > 0 and hp2 > 0:
	#p1 attacks
	print(f"{name1} attacks!")
	wait()
	atk2()
	print(f"{name2} took {atk} damage!")
	print(f"{name1}: {hp1}HP | {name2}: {hp2}HP")
	turns1 += 1
	input("(continue)")
	clear()
	
	#p2 attacks
	print(f"{name2} attacks!")
	wait()
	atk1()
	print(f"{name1} took {atk} damage!")
	print(f"{name1}: {hp1}HP | {name2}: {hp2}HP")
	turns2 += 1
	input("(continue)")
	clear()
	
if hp1 < 0:
	print(f"{name2} wins in {turns1} turns!!")
else:
	print(f"{name1} wins in {turns2} turns!!")

	
	
	

	

	

