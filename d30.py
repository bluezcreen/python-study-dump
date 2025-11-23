import random, os

food = ("Butterscotch pie", "Carrot cake", "Tiramisu", "Brownies", "Sponge cake")
exit = ("no")

while exit != "yes":
	cake = random.choice(food)
	print(f"What do you think of {cake.strip().lower()}?")
	badgood = input("How is it?").strip().lower()
	opinion = input("What's your opinion on it?").strip().lower()
	
	os.system("clear")
	
	print(f"{cake}, {badgood}, {opinion}")
	result = (f"{cake} was so {badgood}, {opinion}")
	print(f"{result:^80}")
	
	exit = input("quit? yes/no").strip().lower()
	os.system("clear")