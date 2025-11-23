#horse race thing
#yet another gambling game. why do i make gambling games? i don't know maybe it's because they're fun and easy to code
from s import rint, d, dc
from textwrap import dedent
#horse1, horse2, horse3 horse4
pos = [0, 0, 0, 0]
	
def progress():
	#progress
	sq = "■"
	prog = dedent(f"""
	-----------
	1. {sq * pos[0]}🐎
	2. {sq * pos[1]}🐎
	3. {sq * pos[2]}🐎
	4. {sq * pos[3]}🐎
	-----------
	""")
	print(prog)
		
	
def main():
	#have a horse move once (get one score) if horseX == 5
	while True:
		#contains random nums
		hx = [ ]
		
		h1 = rint(1,5)
		h2 = rint(1,5)
		h3 = rint(1,5)
		h4 = rint(1,5)
		hx = [h1, h2, h3, h4]
		
		#if any of the horses get 5, pos[horseX] += 1
		progress()
		print("\nsprinting in progress...")
		dc(0.5)
		for i in range(4):
			if hx[i] == 5:
				pos[i] += 1
		
		
		#win case
		if 5 in pos:
			progress()
			winner = pos.index(5) + 1
			print(f"horse {winner} won!")
			break
		
			

main()
