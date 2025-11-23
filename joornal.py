from s import c
print("joornal")
exit = "N"

while True:
	dec = input("1. write to journal\n2. view journal\n")
	c()
	
	if dec == "1":
		while exit == "N":
			prompt = input("Write something...:\n")
			with open("journal.txt", "a") as f:
				f.write(f"\n{prompt}")
			print("\nsaved!")
			
			exit = input("quit? y/n").strip().upper()
			c()
		c()
		
			
	if dec == "2":
		with open("journal.txt", "r") as f:
			print("- journal.txt -")
			print(f.read())
			input()
			c()			