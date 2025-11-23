print("xperimentalmathgame")

n = int(input("your number please"))
score = 0

for i in range(1,11):
	cans = (i * n)
	uans = int(input(f"{i} × {n} = ?"))
	
	if uans == cans:
		print(f"Correct! {i} × {n} is = {cans}!")
		score += 1
	else:
		print(f"Wrong, answer was {cans}")
		
print(f"You got {score} out of 10 correct")