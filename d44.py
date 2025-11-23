import s

print("bingo card")

d = [
[None, None, None],
[None, None, None],
[None, None, None]]

#insert random thing
for r in range(0, 3):
	for c in range(0,3):
		d[r][c] = s.r_int(1,50)
	
def dingo():
		for r in d:
			for m in r:
				print(f"{m:^5}", end=" | ")
			print()
			print("=========================")
		
#certified [DINGO] stamp
d[1][1] = ("DINGO")
cross = 0

while True:
	print()
	dingo()
	call = int(input("what number got called?: "))
	s.delaclear(0.5)
	
	for r in range(len(d)):
		for c in range(len(d[r])):
				if d[r][c] == call:
					d[r][c] = "X"
					cross+=1
					
	if cross == 8:
		print("win")
		break
	
	


				