import random, time, os
#stats
php = 100
ppp = 50
psp = 100
defstance = False
pturn = True
ehp = 200

php = max(0, min(php, 100))
ppp = max(0, min(ppp, 50))
psp = max(0, min(psp, 100))

ehp = min(ehp, 200)

#debuffs
dbsleep = False
dbshock = False
dbnumb = False

#putting the same mechanics from the previous into a function 
#made here is like putting a big bucket filled with rice into a smaller one expecting itll fit
#so here is my haiku to express it

#Bucket of rice
#Put into smaller bucket
#Will not fit in it

#the allmighty, universal combo
def delaclear(x):
	time.sleep(x)
	os.system("clear")
	
def ShowPlayerStat():
	global php, ppp
	print(f"""
	Player
	HP {php}/100
	PP {ppp}/50""")

#Player moveset
def mBattleD():
	x = ["F", "P", "G", "D", "R"]
	print("""
	(F)ight
	(P)SI
	(G)oods
	(D)efend
	(R)un away""")
	y = input(" ").strip().lower()
	if y not in x:
		print("invalid")
		return True
		return y #where do you keep the boolean?
	...