import random
counter = 0

while True:
	qst = random.randint(1,10)
	qst2 = random.randint(1,10)
	cans = (qst * qst2)
	
	ans = int(input(f"What is {qst} × {qst2}?"))
	if ans == cans:
		counter += 1
		print(f"Correct! Your streak is now {counter}")
	else:
		print(f"Oops. You failed. You got {counter} guesses.")
		break
	
	