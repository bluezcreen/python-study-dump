import s
print("blackjack\n")

dealercard = [ ]
playercard = [ ]
def dealer():
	x = s.r_int(1,13)
	dealercard.append(x)
	
def player():
	x = s.r_int(1,13)
	playercard.append(x)
	
#def printlist():
#	for i in range(len(playercard)):
#		print(i)
# how do i make this work
		
dealer()
player()
player()

while sum(dealercard) < 21 and sum(playercard) < 21:
	d = input(f"""
	DEALER
	{dealercard[0]}, ?
	=========
	YOU
	{player""")

