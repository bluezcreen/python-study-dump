from getpass import getpass as input

input("bock bapers bcissors")

#choose your fighter
p1 = input("player 1, select R, P, or S").strip().upper()
p2 = input("player 2, select R, P, or S").strip().upper()
pa = (p1, p2)

#anticheat
if p1 in ("R", "P", "S") and p2 in ("R", "P", "S"):
	test = "y"
else:
	test = "n"
	
#game 
print(f"P1 has {p1}! P2 has {p2}!")

if test == "y":
	if pa in [("R", "R"), ('S', "S"), ("P", "P")]:
		print("It's a draw!")
	elif pa in [("R", "S"), ("S", "P"), ("P", "R")]:
		print("P1 wins!")
	elif pa in [("S", "R"), ("P", "S"), ("R", "P")]:
		print("P2 wins!")
	else:
		pass
	
elif test == "n":
	print("What are you trying to do here???")
else:
	pass

