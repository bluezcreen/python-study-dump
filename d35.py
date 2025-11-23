import time, os
from colorama import Fore, Back, Style

myList = [ ]
name = ("my list")

def printList():
	print(Fore.BLACK + Back.WHITE + f"{name}".center(50))
	print(Style.RESET_ALL)
		
	for index in range(len(myList)):
		print(f"{index + 1}. {myList[index]}")

def delaclear():
	time.sleep(1)
	os.system("clear")
	
while True:
	print(Fore.BLACK + Back.WHITE + "list program 1.0".center(50))
	print(Style.RESET_ALL)
	
	d = input("(0) add name for list\n(1) add\n(2) remove\n(3) view")
	
	#rename list header
	if d == "0":
		print("> add name")
		nn = input("name your list (will be displayed on header): ")
		name = nn
		delaclear()
		
	#add
	if d == "1":
		print("> add item")
		add = input("add new item: ")
		if add in myList:
			print("item already in list")
			delaclear()
			continue
		else:
			print(f"{add} successfully added to {name}")
			myList.append(add)
			delaclear()
			
	#remove
	if d == "2":
		print("> remove item")
		printList()
		remove = input("remove an existing item: ")
		
		if remove not in myList:
			print(f"the item '{remove}' does not exist")
			delaclear()
		else:
			s = input("are you sure? y/n").strip().upper()
			
			if s == "Y":
				myList.remove(remove)
				print(f"{remove} successfully removed from {name}")
				delaclear()
			elif s == "N":
				continue
				delaclear()
			else:
				continue
				delaclear()
				
	#view
	if d == "3":
			delaclear()
			printList()
			input("input to dismiss")
			delaclear()
			
	else:
			continue
			delaclear()
			
		
	
		
	
		
	
	
	