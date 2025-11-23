exit = " "

while exit != "yes":
	
	answ = input("is mother 3 a good game (yes/no)").strip().lower()
	if answ == "yes":
		print("based") 
	elif answ == "no":
		print("oh ok")
	else:
		pass
	
	exit = input("exit?").strip().lower()