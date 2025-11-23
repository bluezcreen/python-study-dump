import s
#i did not know this existed
def question():
	qes = (s.r_int(1, 10), s.r_int(1,10))
	a,b = qes
	ans = (a + b)
	print(f"{a} + x = {ans}\nx?")
	return b
	
exit = False
while not exit:
	#random questions
	question()
	
	uans = input("answer: ")
	
	thing = question()
	match qes:
		case b:
			print("correct")
		case _:
			print("wrong")
			continue
