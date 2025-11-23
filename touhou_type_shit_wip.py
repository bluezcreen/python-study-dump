import random

a1 = a2 = a3 = b1 =  b2 = b3 = c1 = c2 = c3 = ("HIT!")

grid = [a1, a2, a3, b1, b2, b3, c1, c2, c3]

bullets = random.sample(grid, 8)

for v in grid:
	if v not in bullets:
		print(f"{v} is safe")

#def bulletvisualize():
#	if 
#bullets = bulletmake()
#print("""
#╔═╦═╦═╗
#║a1║a2║a3║
#╠═╬═╬═╣
#║b2   b2║b3║
#╠═╬═╬═╣
#║c1║c2║c3║
#╚═╩═╩═╝
#""")

#player = input("choose a tile")

#if player in bullets:
#	print(f"bro got hit({player})")
#else:
#	print("bro didn't got hit")
