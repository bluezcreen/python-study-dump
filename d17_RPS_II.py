from getpass import getpass as input
import sys

print("bock bapers bcissors II")

#game 

counter = 0
p1s = 0
p2s = 0
while True:
		
	#choose your fighter
		p1 = input("player 1, select R, P, or S").strip().upper()
		p2 = input("player 2, select R, P, or S").strip().upper()
		pa = (p1, p2)
		
		#anticheat
		if p1 in ("R", "P", "S") and p2 in ("R", "P", "S"):
			test = "y"
		else:
			test = "n"
			
		if pa in [("R", "R"), ('S', "S"), ("P", "P")]:
			print("It's a draw!")
		elif pa in [("R", "S"), ("S", "P"), ("P", "R")]:
			print("P1 wins!")
			p1s += 1
		elif pa in [("S", "R"), ("P", "S"), ("R", "P")]:
			print("P2 wins!")
			p2s += 1
			
		if test == "y":
			counter += 1
			print(f"Round {counter}")
			print(f"P1 has {p1}! P2 has {p2}!")
			print(f"P1: {p1s} | P2: {p2s}")
			if p1s < 3 or p2s < 3:
				continue
			elif p1s == 3:
				sys.exit("P1 wins!")
			elif p2s == 3:
				sys.exit("P2 wins!" )
		
		elif test == "n":
			print(f"P1 has {p1}! P2 has {p2}!")
			print("What are you trying to do here???")
			continue
	
		else:
			pass
	
