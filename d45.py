import s, time, random, os
from colorama import Fore, Back, Style

tasks = [ ["name", "description", "priority"] ]
pri = ["high", "medium", "low"]

def printlist(): 
	print(Fore.BLACK + Back.WHITE + "your current tasks".center(83))
	print(Style.RESET_ALL)
	for row in tasks:
		for item in row:
			print(f"{item:^25}", end=" | ")
		print()
		
def printpriority(x):
	global pri
	if x in pri:
		
while True:
	print("task manager++\n")
	x = input("(1) add\n(2) remove\n(3) edit\n(4) view")
	
	#add
	if x == "1":
		s.delaclear()
		print("add a task")
		taskn = input("label: ")
		taskd = input("description: ")
		taskp = input("priority:\n(1) high\n(2) medium\n(3) low\n")
		
		if taskp in pri:
			append = [taskn, taskd, taskp]
		else:
			continue
		
		if append not in tasks:
			tasks.append(append)
			print(f"added to list\n")
			printlist()
			s.delaclear(0, True)
		else:
			print("duplicate error")
			s.delaclear(1)
			continue
			
	#remove
	elif x == "2":
		print("remove a row\n")
		printlist()
		o = int(input("remove a row in list: "))
		
		if o < len(tasks):
			#confirm?
			c = input(f"are you sure to remove the item? yes/no")
			if c.lower() == "yes":
				del tasks[o]
				print("item removed")
				s.delaclear(1)
			else:
				print("index out of range")
				s.delaclear(1)
				continue
	
	#edit
	elif x == "3":
		printlist()
		p = int(input("choose a row to edit: "))	
		
		if p < len(tasks):
			t = input("change name: ")
			u = input("change description: ")
			v = input("change priority\n(1) high\n(2) medium\n(3) low\n")
			replace = [t, u, v]
			
			if taskp in pri:
				tasks[p] = replace
				print(f"row {p} replaced")
				s.delaclear(1)
			else:
				continue
		
		else:
			print("index out of range")
			s.delaclear(1)
			continue
						
	elif x == "4":
		printlist()
		input()
		s.delaclear()
		
	else:
		s.delaclear()
		continue
		
		
		
		