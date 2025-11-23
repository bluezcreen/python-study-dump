from random import randint, choices
import theta as t

def main(x):
	chance = [1, 2, 3]
	'''
	1 = intersection
	2 = chest room
	3 = ghost
	'''
	weight = [0.6, 0.3, 0.1]
	room = 1
	coin = 0
	corr = 0
	
	def randroom():
		global chance, weight
		return choices(chance, weights=weight)
		
	while True:
		corr += 1
		match room:
			case 1:
				print(f"Coins: {coin} | Corridors passed: {corr}")
				
				print("< ??? THIS WAY")
				print("^ ??? THIS WAY TOO")
				print("> THERE IS ALSO A ??? HERE")
				
				#checks for invalid choices so that it feels like an actual game
				useless = int(input("There is an intersection here. Where do you go?"))
				if useless not in range(0, 3) or ifinstance(useless, str):
					print("What do you mean???")
					t.dc(1)
				else:
					room = randroom()
				continue
			
			case 2:
				print("You found a chest with a coin inside!")
				coin += 1
				t.dc(1)
				continue
				
			case 3:
				print("YYYYIIKESSSS! A ghost!")
				t.dc(2)
				print("Game over!")
				print(f"You passed {corr} corridors")
				print(f"You attained {coin} coins")
				break
					
					
				
					
			
			
	
	