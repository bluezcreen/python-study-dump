import random, time, os, s

print("top trumps (what kind of game is that? never heard of it)\n")

chara = {
"john" : {
"ATK" : 89,
"DEF" : 42,
"PWR" : 79},

"jim" : {
"ATK" : 77,
"DEF" : 62,
"PWR" : 67},

"jack" : {
"ATK" : 92,
"DEF" : 44,
"PWR" : 12},

"joe" : {
"ATK" : 44,
"DEF" : 97,
"PWR" : 33}
}
p1c = 0
p2c = 0
cont = False
exit = False
p1 = None
p2 = None
stat = None

def printkeys():
	for name in chara.keys():
		print(name)
	
def compare(x, y, z):
	global p1c, p2c
	#x = p1, y = p2, z = stat
	print(f"p1: {chara[x][z]}\np2: {chara[y][z]}\n {p1c} / {p2c}")
	
	if chara[x][z] > chara[y][z]:
		print("p1 wins")
		p1c += 1
		s.delaclear(1)
	else:
		print("p2 wins")
		p2c += 1
		s.delaclear(1)
		
def charachoose():
	global p1, p2, stat, cont
	thing = ["ATK", "DEF", "PWR"]
	
	printkeys()
	p1 = input("p1 | choose a character: ").strip().lower()
	if p1 not in chara:
		print("invalid choice")
		cont = True
		s.delaclear(1)
		return
		
	s.delaclear()
	
	printkeys()
	p2 = input("p2 | choose a character: ").strip().lower()
	if p2 not in chara:
		print("invalid choice")
		cont = True
		s.delaclear(1)
		return
		
	s.delaclear()
	
	stat = input("what to compare? atk/def/pwr: ").strip().upper()
	if stat not in thing:
		print("invalid choice")
		cont = True
		s.delaclear(1)
		
	else:
		cont = False
#choose a character
while exit != "exit":
	charachoose()
	if cont:
		continue 
	exit = ("input exit to exit, anything else to continue")
	compare(p1, p2, stat)



	