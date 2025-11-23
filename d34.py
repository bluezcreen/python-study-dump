import time, os
emails = [ ]

def clear():
	os.system("clear")

def printList():
	print("EMAILS LISTED")
	
	for index in range(len(emails)):
		print(f"{index + 1}: {emails[index]}")
		
	time.sleep(2)
	os.system("clear")
	
def writeEmail():
	clear()
	for index in range(len(emails)):
		input(f"WRITE [You've got mail!]\n {index + 1}: {emails[index]}")
		clear()
		
	

	
while True:
	a = input("[BIGSHOT] SPAM MACHINA\n 1. ADD VICTIM\n 2. SPARE VICTIM\n 3.SEE MY VICTIMS\n 4. [BUSINESS]")
	if a == "1":
		add = input("ADD A VICTIM: ")
		emails.append(add)
		clear()
	elif a == "2":
		remove = input("SPARE A VICTIM: ")
		if remove in emails:
			emails.remove(remove)
		else:
			print("THAT ISN'T ON THE LIST YOU [Error 404]")			
	elif a == "3":
		printList()
	elif a == "4":
		writeEmail()
	else:
		continue