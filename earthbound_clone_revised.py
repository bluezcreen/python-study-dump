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
def mMenu():
	print("""
	(F)ight
	(P)SI
	(G)oods
	(D)efend
	(R)un away""")

def mFight():
	global ehp, pturn
	print("Player attacks!")
	patk = random.randint(8,28)
	ehp -= patk
	print(f"Enemy took {patk} damage!")
	pturn = False

def mPSI():
	print("""
	* Offense
	(PK) Love - 10PP
	(S)uicide - free
	(I)nstakill - free
	
	* Assist
	(L)ifeup - 5PP
	(P)aralysis - 10PP
	(H)ypnosis - 8PP
	(B)rainshock - 10PP
	
	* Other
	(S)hield - 10PP
	(C)ounter - 14PP""")

def mGoods():
	pass
	pturn = True
	#soon
	
def mDefend():
	global defstance, pturn
	print("Player is defending.")
	defstance = True
	pturn = False
	
def mRun():
	global pturn, dbsleep, dbnumb, ehp
	print("Player tried to run..")
	
	if dbsleep == True or dbnumb == True:
		print("...and did!")
		ehp = 0
	else:
		x = random.randint(1,2)
		if x == 1:
			print("...but couldn't!")
			pturn = False
		else:
			print("...and did!")
			ehp = 0
	
#Damage model
def PlayerDMGM(hpl=0, ppl=0, spl=0):
	global php, ppp, psp
	php -= hpl
	ppp -= ppl
	psp -= spl

def EnemyDMGM(hpl=0):
	global ehp
	ehp -= hpl
	#enemy pp and psi moveset soon

#Moveset
def EnemyMoveset():
	x = random.randint(1,4)
	global defstance, pturn
	
	if pturn == False:
		if x <= 1:
			print('Enemy is being absentminded.')
			pturn = True
		else:
			if defstance == False:
				print("Enemy attacks!")
				edmg = random.randint(10,30)
				PlayerDMGM(eatk)
				print(f"Player took {eatk} damage!")
				pturn = True
			else:
				print("Enemy attacks!")
				edmg = random.randint(10,30)
				PlayerDMGM(eatk * (10/100))
				print(f"Player took {eatk} damage!")
				pturn = True


#battle
while ehp != 0 or php != 0:
	if pturn == False:
		EnemyMoveset()
	else:
		mMenu()
		ShowPlayerStat()
		decision = input("Choose a move").upper()
		pdec(decision)
	
	if ehp == 0:
		delaclear(0.5)
		print("YOU WON!")
		break
		
	elif php ==  0:
		print("Player got hurt and collapsed...")



	