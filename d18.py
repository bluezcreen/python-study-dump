import random
counter = 0
answer = random.randint(1,100)
	
while True:
	guess = int(input("Guess a number from 0 to 100"))
	
	if guess == answer:
		print(f"Correct! You took {counter} attempts to guess!")
		exit()
	elif guess >= answer:
		print("Too high")
		counter += 1
	elif guess < answer:
		print("Too low")
		counter +=1
	elif guess <= 0:
		exit('You discovered something hidden')
	