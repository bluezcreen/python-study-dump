import s


while True:
	letter = input("match/case test | select letter from a-e").strip().upper()
	
	match letter:
		case "A":
			print("alpha")
			s.delaclear(1)
			
		case "B":
			print("beta")
			s.delaclear(1)
			
		case "C":
			print("c")
			s.delaclear(1)
			
		case "D":
			print("delta")
			s.delaclear(1)
			
		case "E":
			print("epsilon")
			s.delaclear(1)
			
		case _:
			print("what?")
			s.delaclear(1)