aList = [ ]

def printlist():
	print("your current list\n")
	for i in aList:
		print(i.title())
		
#ultimatum 
def delaclear(x=0):
	import time, os
	time.sleep(x)
	os.system("clear")
	
while True:
	print("fone-tact | a phonebook contact that doesnt even have phone numbers\n")
	x = input("(1) add\n(2) remove\n(3) view")
	
	#add
	if x == "1":
		print("add a name")
		FN = input("first name: ")
		LN = input("last name: ")
		N = (FN + " " + LN).strip().lower()
		
		if N not in aList:
			z = (FN + " " + LN).strip().title()
			print(f"'{z}' added to list\n")
			aList.append(N)
			printlist()
			delaclear(1)
		else:
			print("duplicate error")
			delaclear(1)
			continue
			
	#remove
	elif x == "2":
		print("remove a name\n")
		printlist()
		o = input("remove name in list: ").strip().lower()
		
		if o.lower() in aList:
			#confirm?
			c = input(f"are you sure to remove the item? yes/no")
			if c.lower() == "yes":
				aList.remove(o)
				print("item removed")
				delaclear(1)
			else:
				delaclear(1)
				continue
				
	elif x == "3":
		printlist()
		input()
		delaclear()
		
	else:
		delaclear()
		continue
		
		
		
		