import s
print("hangman\n")
words = ["world"]
lifes = (5)
#words = ["variable", "programming", "function", "tuple", "list", "module", "indent", "fstring", "loop", "print"]

#x = s.r_int(0, 9)
answer = words[0]
	
#give word
progress = ["_"] * len(answer)
		
guess = " "

while lifes > 0:
	guess = input("guess a letter from the word").strip().lower()
	g = (guess[0])
	print(g)
	print(answer)
	
	for i, letter in enumerate(answer):
		if g in letter:
			progress[i] = g
			s.delaclear()
			
			for j in progress:
				print(j, end=" ")
		
		else:
			print("wrong")
			lifes -= 1
			print(f'{lifes} lifes left')
				
	#FUCK
