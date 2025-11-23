#gambling simulator 
import random, os, time,pygame
from collections import Counter
from colorama import Fore, Back, Style
#music 
from playsound import playsound
import threading

def play_music():
    while True:
        playsound("Welcome to the Green Room.mp3")
threading.Thread(target=play_music, daemon=True).start()

#stuff
symb = ["🍒", "🍋", "🪙", "💲", "7️⃣", "💎"]
money = 100
n = 3
reward = 0

def spinny(x):
	for i in x:
		print(i, end=" ")
		
def title():
	print(Fore.BLACK + Back.WHITE + "slot machine".center(80))
	print(f"balance: ${money}".center(80))
	print(Style.RESET_ALL)
	
def delaclear(x=1):
	time.sleep(x)
	os.system("clear")
	
exit = ("N")

while exit == "N":
	title()
	#bet
	y = int(input("how many spins?\n1 spin = $10: "))
	
	spent = 10 * y
	money -= spent
	
	#speed up rolling if spins > 15
	if y >= 15:
		n = 1
	elif y >= 30:
		n = 0.1
	elif y >= 50:
		n = 0
		
	print(f"spent ${spent}")
	delaclear(1)
	
	#roll
	for x in range(y):
		title()
		
		spin = (random.choices(symb, k=5))
		spinny(spin)
		
		print(Style.RESET_ALL)
		counts = Counter(spin) 
		
		reward = 0
		for symbol, count in counts.items():
			if count == 2:
				pass
				#no money for you
				
			if count == 3:
				print(f"triple topple: {symbol}")
				reward += 10
				
			if count == 4:
				print(f"rent for the next 2 months in new york: {symbol}")
				reward += 25
				
			if count == 5:
				print("jackpot! now you can buy a box of eggs in the united states!!!")
				reward += 500
				
			if count >= 3:
				print(f"you won ${reward}.00!")
				
		money += reward
		delaclear(n)
		
	#reward
	title()
	if money <= 0:
		print(f"you are currently in debt: {money}")
	
	exit = input("quit? y/n: ").strip().upper()
	delaclear(0)
	

