import s

heldcards = [ ]
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
blind = (1000)
chips = 0

def fetchcards():
	heldcards.append(s.r_sample(cards))
	
def game():
	print(f"""
	jokers
	+10 mult | X2 mult
	
	{heldcards}""")
	
def gencards():
	for i in range(1, 9):
		fetchcards()
		
	
def addcards():
	x = 8 - heldcards
	for i in range(x+1):
		fetchcards()
		
gencards()
while chips < blind:
	game()
	r = input("choose a ")
	
	