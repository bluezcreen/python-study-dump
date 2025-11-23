from colorama import Fore, Back, Style
import os, time

grocery = []

def delaylear():
	time.sleep(1)
	os.system("clear")
	
def actions():
	global grocery
	
	while True:
		z = input("add/remove/view: ").strip().lower()
		
		if z == "add":
			a = input("add an item: ")
			grocery.append(a)
			print(f"{a} added to grocery list")
			delaylear()
		
		elif z == "remove":
			for items in grocery:
				print(items)
			r = input("remove an item:")
			
			if r in grocery:
				grocery.remove(r)
				print(f"{r} removed from grocery list")
				delaylear()
			else:
				print("this item isn't even in the list")
				delaylear()
				
		elif z == "view":
				print(Fore.BLACK + Back.WHITE + "grocery list".center(80))
				print(Style.RESET_ALL)
				for items in grocery:
					print(items)
				
				input()
				os.system("clear")
				continue
				
		else:
			continue
	
actions()