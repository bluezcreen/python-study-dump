n = int(input("pick a number: "))
conj = [ ]
conj.append(n)
#n ≠ conj, it only serves as a record

while n > 1:
	#if n is even, half it
	if n % 2 == 0: #even
		n //= 2
		conj.append(n)
	else: #odd
		n = ((3*n) + 1)
		conj.append(n)
		
for i in conj: print(i, end=" > ")
		
	