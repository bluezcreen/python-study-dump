import random, time

print("roulette dx++ omega alpha beta gamma luxury professional mega giga 1+2+3+4 edition\n")

wheel = [" "]
#1 = number, 2 = color, 3 = twelves, 4 = odd/even, 5 = halves
def roll():
	n = random.randint(0, 36)
	wheel.append(n)
	#assign color
	if n % 2 == 0:
		wheel.append("black")
	else:
		wheel.append("red")

def oddeven(x):
	if x % 2 == 0:
		wheel.append("odd")
	else:
		wheel.append("even")
	
def twelves(x):
	if x in range(0, 12):
		wheel.append("1")
	elif x in range(13, 24):
		wheel.append("2")
	elif x in range(25, 36):
		wheel.append("3")

def halves(x):
	if x <= 19:
		wheel.append("A")
	elif x > 19:
		wheel.append("B")

def wheelcheck(x, y):
	if x == wheel[y]:
		print("You win!")
	else:
		print("You lost")
				
def bets(x):
	
	if x == "1":
		n = int(input("pick a number between 0-36"))
		if 0 <= n >= 36:
			wheelcheck(n, 1)
		else:
			return False
			
		return True
	
	elif x == "2":
		o = input("which color? red/black").strip().lower()
		if o == wheel[2]:
			print("You win!")
		else:
			print('You lost')
			
	elif x == "3":
		p = input("which twelves?\n (1) 1st twelves\n (2) 2nd twelves\n (3) 3rd twelves")
		if p == wheel[3]:
			print("You win!")
		else:
			print("You lost")
			
	elif x == "4":
		#odd/even is literally the same as black/red lmao
		q = input("odd/even").strip().lower()
		if q == wheel[4]:
			print("You win!")
		else:
			print("You lost")
	
	elif x == "5":
		r = input("which half? (A) first (B) second")
		if q == wheel[5]:
			print("You win!")
		else:
			print("You lost")
			
#checky thingy
roll() 
x = wheel[1]#1
twelves(x)#2
halves(x)#3
oddeven(x)#4

print("(1) 0 to 36\n(2) red/black\n(3) 1st twelves/2nd twelves/3rd twelves\n(4) odd/even\n(5) 0-19/20-36")
b = input("choose a bet")


bets(b)
for i in wheel:
	print(i, end=" ")




